#!/usr/bin/python
import json
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--file-location", action="store", dest="file_location", help="Full path to the cli-scan.json produced by Polaris Scan", default=".synopsys/polaris/cli-scan.json")
parser.add_argument("--max-total", action="store", dest="total_allowed", help="Maximum number of issues in total before failing the job", type=int, default=0)
parser.add_argument("--max-critical", action="store", dest="critical_allowed", help="Maximum number of Critical Severity issues before failing the job", type=int, default=0)
parser.add_argument("--max-high", action="store", dest="high_allowed", help="Maximum number of High Severity issues before failing the job", type=int, default=0)
parser.add_argument("--max-medium", action="store", dest="medium_allowed", help="Maximum number of Medium Severity issues before failing the job", type=int, default=0)
parser.add_argument("--max-low", action="store", dest="low_allowed", help="Maximum number of Low Severity issues before failing the job", type=int, default=0)

args = parser.parse_args()

class PolarisResults:
    def __load_file(self):
        try:
            f = open(self.file_location, mode='r')
            self.json_data = json.load(f)
        except FileNotFoundError:
            print('Cannot find file:{0}'.format(self.file_location))
            sys.exit(10)
        except json.JSONDecodeError as e:
            print('Cannot parse json data. Reason:{0}'.format(e.msg))
            sys.exit(20)
        finally:
            f.close()

    def __validate_set_required_fields(self):
        self.summary_url = self.json_data['issueSummary']['summaryUrl']
        self.job_status = self.json_data['tools'][0]['jobStatus']
        self.total_issues = int(self.json_data['issueSummary']['total'])
        self.critical_issues = int(self.json_data['issueSummary']['issuesBySeverity']['critical'])
        self.high_issues = int(self.json_data['issueSummary']['issuesBySeverity']['high'])
        self.medium_issues = int(self.json_data['issueSummary']['issuesBySeverity']['medium'])
        self.low_issues = int(self.json_data['issueSummary']['issuesBySeverity']['low'])

    def __init__(self, file_location):
        self.file_location = file_location
        self.__load_file()
        self.__validate_set_required_fields()

if __name__ == "__main__":
    exit_code = 0

    results = PolarisResults(args.file_location)

    if results.job_status != "COMPLETED":
        print(f"Polaris SAST scan failed for some reason, all we know is '{results.job_status}'")
        sys.exit(1)

    # Run checks against each of the thresholds
    print(f"-----------------------------------------------------------")
    print(f"|                        RESULTS                           |")
    print(f"------------------------------------------------------------")
    if results.total_issues > args.total_allowed:
        print(f"❌ TOTAL ISSUES = {results.total_issues} (threshold = {args.total_allowed})")
        exit_code = 1
    else:
        print(f"✅ TOTAL ISSUES = {results.total_issues} (threshold = {args.total_allowed})")

    if results.critical_issues > args.critical_allowed:
        print(f"❌ CRITICAL SEVERITY ISSUES = {results.critical_issues} (threshold = {args.critical_allowed})")
        exit_code = 1
    else:
        print(f"✅ CRITICAL SEVERITY ISSUES = {results.critical_issues} (threshold = {args.critical_allowed})")

    if results.high_issues > args.high_allowed:
        print(f"❌ HIGH SEVERITY ISSUES = {results.high_issues} (threshold = {args.high_allowed})")
        exit_code = 1
    else:
        print(f"✅ HIGH SEVERITY ISSUES = {results.high_issues} (threshold = {args.high_allowed})")

    if results.medium_issues > args.medium_allowed:
        print(f"❌ MEDIUM SEVERITY ISSUES = {results.medium_issues} (threshold = {args.medium_allowed})")
        exit_code = 1
    else:
        print(f"✅ MEDIUM SEVERITY ISSUES = {results.medium_issues} (threshold = {args.medium_allowed})")

    if results.low_issues > args.low_allowed:
        print(f"❌ LOW SEVERITY ISSUES = {results.low_issues} (threshold = {args.low_allowed})")
        exit_code = 1
    else:
        print(f"✅ LOW SEVERITY ISSUES = {results.low_issues} (threshold = {args.low_allowed})")

    if exit_code > 0:
        print(f"\n\n❌ Job failed: Please review the findings at: {results.summary_url}")
        print("Push some fixes and be a hero for the team!")
        sys.exit(1)
    else:
        print("\n\n✅  Awesome - your code seems to be in good shape! ✅ ")
        print("Please take a moment to review the thresholds and see if they can be lowered even further!")
        sys.exit(0)
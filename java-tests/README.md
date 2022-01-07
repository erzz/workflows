# Java-Tests Workflow Overview <!-- {docsify-ignore-all} -->

## Purpose

This workflow is, very specifically, based on a case where we are building a Maven application, possibly with a Maven settings file and possibly needing some GCP authentication elements during testing.

?>There may be other variations of this in the future - feel free to request!

In general it will run Unit Tests, Code Quality and SAST for the build.

- Code Quality using Code Climate in standalone mode
  - Default configuration or bring your own
  - Configurable Pass / Fail criteria
  - HTML report as artifact by default
- Polaris SAST Scan
  - Provides results analysis script to "break the build" on your own criteria
  - Option to include maven settings file
  - JSON report as an artifact
  - Optional usage of a maven-settings.xml
- Unit Tests
  - Option to provide GCP auth via SA key or OIDC
  - Configurable test command
  - Provides Surefire and Jacoco reports as artifacts
  - Optional usage of a maven-settings.xml

## Included Jobs

```mermaid
%%{init: {'theme': 'neutral'}}%%

flowchart LR
  subgraph Pre-Requisites
    subgraph Mandatory
      jacoco>"jacoco\n(Maven Dependency)"]
      surefire>"surefire\n(Maven Dependency)"]
      polaris>"Polaris URL & key\n(Secrets)"]
    end
    subgraph Optional
      mvn-settings>"maven-settings.xml\n(Secret)"]
      gcp-sa>"GCP Service Account\nJSON Key (Secret)"]
      gcp-oidc>"GCP Identity Provider +\nService Account\n(Secret)"]
    end
  end
  subgraph Jobs
    code-quality{"Code Climate\nStandalone"}
    polaris-sast{"Polaris SAST"}
    unit-tests{"Custom\nUnit Tests"}
  end
  subgraph Artifacts
    subgraph Code Quality
      cc-html["codeclimate-report.html"]
      cc-json["codeclimate-report.json"]
    end
    subgraph SAST
      report-polaris-json["cli-scan.json"]
      report-polaris-server["Polaris Report\n(Server)"]
    end
    subgraph Unit Test Results
      surefire-xml["Surefire XML reports"]
    end
    subgraph Code Coverage
      jacoco-html["JaCoCo HTML"]
      jacoco-xml["JaCoCo XML"]
      jacoco-csv["JaCoCo CSV"]
    end
  end

  %% dependencies -> Jobs
  jacoco-->|mandatory|unit-tests
  surefire-->|mandatory|unit-tests
  mvn-settings-.->|optional|unit-tests
  gcp-sa-.->|optional|unit-tests
  gcp-oidc-.->|optional|unit-tests
  polaris-->|mandatory|polaris-sast

  %% Jobs -> Reports
  code-quality-->cc-html
  code-quality-->cc-json
  unit-tests-->surefire-xml
  unit-tests-->jacoco-html
  unit-tests-->jacoco-xml
  unit-tests-->jacoco-csv
  polaris-sast-->report-polaris-json
  polaris-sast-->report-polaris-server
```

### Code Climate Standalone

Runs a version of Code Climate that requires no subscription or server connection. Just executes locally using either this workflow's configuration or you own to identify code quality, consistency and good practice.

**Uses:** [erzz/codeclimate-standalone@v0.0.3](https://github.com/erzz/codeclimate-standalone)

### Polaris SAST

!> This is a paid service and you will be expected to provide both the URL and an access key to send your results to Synopsis for analysis

SAST application that analyses your code for security issues and bad practices

**Uses:** N/A Scripted installation and execution in the workflow

### Unit Tests

!> You will need to provide your own tests. This job automates the execution of your `mvn test --fail-at-end -B` (or equivalent) command and produces reports plus coverage

Executes your Unit tests with a command of your choice and provides reports from Surefire plus Code Coverage from JaCoCo

Uses: N/A Scripted installation and execution in the workflow
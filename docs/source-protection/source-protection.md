# Source Protection Release Workflow

## Usage

Simply include the workflow within your project's workflow using something like the following.

```yaml
source-protection:
  uses: erzz/workflows/.github/workflows/source-protection.yml@main
```
## Secrets

None at this time

## Inputs

| Input                    | Required | Default                 | Details                                                                                                           |
| ------------------------ | -------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `creds-scan-directory`   | false    | `''`                    | Defaults to the repository root - specify your own path if required                                               |
| `creds-fail-build`       | false    | `true`                  | Defaults to failing the job if tests do not pass. Set to false for the opposite (yet not recommended!) behaviour" |
| `creds-fetch-depth`      | false    | `50`                    | How many commits to fetch from the repo. Set to 0 for all (slow!) - but at least a minimum of 2                   |
| `creds-gitleaks-config`  | false    | `.gitleaks.toml`        | Path to a custom gitleaks config if required                                                                      |
| `commits-enable`         | false    | `true`                  | Set to false if you want to disable the commit lint job                                                           |
| `commits-default-config` | false    | `true`                  | This workflow provides a commit lint config based on conventional commits. Set to false to use your own           |
| `commits-config-file`    | false    | `.commitlint.config.js` | Relative path to your own configuration for commit lint if not using the default                                  |
| `commits-fail-build`     | false    | `true`                  | Set to false if you do not want commit lint to fail on warnings                                                   |

## Outputs

None at this time

## Other Examples

### Run only the credential scanning jobs

Useful when running as part of a production deploy when there are no new commits.

```yaml
source-protection:
  uses: erzz/workflows/.github/workflows/source-protection.yml@main
  with:
    commits-enable: false
```


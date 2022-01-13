# Go Tests Workflow

## Basic

Go provides great tooling out of the box and thus you can likely use something as simple as:

```yaml
go-tests:
  uses: erzz/workflows/.github/workflows/go-tests.yml@go-tests
```

## Secrets

None at this time

## Inputs

!> the `go-version` input is currently disabled due to an issue with the `setup-go` action within reusable workflows.

| Input                   | Required | Default            | Details                                                                                 |
| ----------------------- | -------- | ------------------ | --------------------------------------------------------------------------------------- |
| `go-version`            | disabled | disabled           | Select the version of go to use. Accepts https://github.com/npm/node-semver             |
| `cc-default-config`     | false    | `true`             | Set to false if you want to use your own .codeclimate.yml config                        |
| `cc-config-file`        | false    | `.codeclimate.yml` | Set relative path to your own code climate configuration if `cc-default-config`=`false` |
| `cc-info-threshold`     | false    | `0`                | Max number of INFO Code Climate findings allowed before forcing a failed result         |
| `cc-minor-threshold`    | false    | `0`                | Max number of MINOR Code Climate findings allowed before forcing a failed result        |
| `cc-major-threshold`    | false    | `0`                | Max number of MAJOR Code Climate findings allowed before forcing a failed result        |
| `cc-critical-threshold` | false    | `0`                | Max number of CRITICAL Code Climate findings allowed before forcing a failed result     |
| `cc-blocker-threshold`  | false    | `0`                | Max number of BLOCKER Code Climate findings allowed before forcing a failed result      |
| `gosec-default-config`  | false    | `true`             | Set to false if you want to use your own `.gosec-config.json`                           |
| `gosec-scan-path`       | false    | `./...`            | Set a custom path for gosec to scan if required                                         |
| `unit-test-path`        | false    | `./...`            | Set a custom path for the go test command if required                                   |

## Outputs

None

## Advanced Examples

### Using a specific Go version

```yaml
go-tests:
  uses: erzz/workflows/.github/workflows/go-tests.yml@go-tests
  with:
    go-version: 1.16.2
```

### Set your own Code Quality thresholds

```yaml
go-tests:
  uses: erzz/workflows/.github/workflows/go-tests.yml@go-tests
  with:
    cc-info-threshold: 5
    cc-minor-threshold: 3
    cc-major-threshold: 0
    cc-critical-threshold: 0
    cc-blocker-threshold: 0
```

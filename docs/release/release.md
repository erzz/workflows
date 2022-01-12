# Semantic Release Workflow

## Basic

Simply include the workflow within your project's workflow using something like the following.

?> `on.workflow_dispatch` in this example means you intend to run the workflow manually. You can just as easily add the job into an automated flow instead where the job would run automatically or any other combination of release process.

```yaml
name: Release
on: workflow_dispatch
jobs:
  release:
    uses: erzz/workflows/.github/workflows/semantic-release.yml@main
    secrets:
      token: ${{ secrets.RELEASE_TOKEN }}
```

## Secrets

| Input                 | Required | Details                                                                                             |
| --------------------- | -------- | --------------------------------------------------------------------------------------------------- |
| `token`               | true     | A secret containing a GITHUB_TOKEN with permissions to create releases, push directly to master etc |
| `maven-settings-file` | false    | If a maven settings file is required provide the secret containing the file                         |

## Inputs

| Input            | Required | Default | Details                                                                                        |
| ---------------- | -------- | ------- | ---------------------------------------------------------------------------------------------- |
| `default-config` | false    | `true`  | If you have your own .releaserc.json already in you project - set this input to `false`        |
| `mvn-settings`   | false    | `false` | Should combine with `default-config: false` and special pom.xml updating config will be used   |
| `dry-run`        | false    | `false` | Used to only preview the release result and notes for testing. Set to true to enable           |

## Outputs

| Output                | Description                                                | Example value                          |
| --------------------- | ---------------------------------------------------------- | -------------------------------------- |
| new_release_published | Returns true if a release was created                      | `true`                                 |
| new_release_version   | The version given to the release if created                | `v1.2.0`                               |
| new_release_notes     | The contents of the release notes if a release was created | The full markdown of the release notes |

## Advanced Examples

### Use your own configuration

```yaml
release:
  uses: erzz/workflows/.github/workflows/semantic-release.yml@main
  with:
    default-config: false
  secrets:
    token: ${{ secrets.RELEASE_TOKEN }}
```

### Maven projects and using a maven settings file

With this combination of `mvn-settings: true` and `mvn-settings-file:` a special version of the workflow will run which will give the ability to both set a maven-settings file plus a semantic-release configuration that also updates pom.xml with the newly released version.

```yaml
release:
  uses: erzz/workflows/.github/workflows/semantic-release.yml@main
  with:
    default-config: false
    mvn-settings: true
  secrets:
    token: ${{ secrets.RELEASE_TOKEN }}
    mvn-settings-file: ${{ secrets.MAVEN_SETTINGS_FILE }}
```
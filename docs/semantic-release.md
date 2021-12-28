# Semantic Release

![Semantic-Release Workflow](/media/semantic-release.png)

This workflow will:

- Analyze your semantic commit git history, and create a semantically versioned release if required (uses [cycjimmy/semantic-release-action@v2.7.0](https://github.com/cycjimmy/semantic-release-action))
- Provides a [standard configuration](/.github/workflows/semantic-release-config.json) with option to disable and use the config already in your repository.

# Usage

Simply include the workflow within your project's workflow using something like the following.

**Note:** `on.workflow_dispatch` in this example means you intend to run the workflow manually. You can just as easily add the job into an automated flow instead where the job would run automatically or any other combination of release process.

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

| Input   | Required | Default        | Details                                                                                             |
| ------- | -------- | -------------- | --------------------------------------------------------------------------------------------------- |
| `token` | true     | N/A - REQUIRED | A secret containing a GITHUB_TOKEN with permissions to create releases, push directly to master etc |

## Inputs

| Input            | Required | Default | Details                                                                                 |
| ---------------- | -------- | ------- | --------------------------------------------------------------------------------------- |
| `default-config` | false    | `true`  | If you have your own .releaserc.json already in you project - set this input to `false` |

## Outputs

| Output                | Description                                                | Example value                          |
| --------------------- | ---------------------------------------------------------- | -------------------------------------- |
| new_release_published | Returns true if a release was created                      | `true`                                 |
| new_release_version   | The version given to the release if created                | `v1.2.0`                               |
| new_release_notes     | The contents of the release notes if a release was created | The full markdown of the release notes |

# Other Examples

## Run the job with a configuration already in your repo

```yaml
release:
  uses: erzz/workflows/.github/workflows/semantic-release.yml@main
  with:
    default-config: false
  secrets:
    token: ${{ secrets.RELEASE_TOKEN }}
```
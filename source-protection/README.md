# Source Protection Workflow Overview

## Purpose

Jobs that catch credentials being committed to source or commit messages that do not follow the team's convention. Both issues are easy to rectify when caught quickly but somewhat more complex to handle if not.

This workflow will check your repository for:

- accidentally committed credentials and secrets
- optionally validate the commit history for adherence to conventional commit practices

!> This workflow is intended to be run early (from first push to a branch) in order to catch issues with your repository **EARLY** when they are easy to fix! To run the jobs on every push, put them in a workflow that executes `on.push`

## Included Jobs

```mermaid
%%{init: {'theme': 'neutral'}}%%

flowchart LR
  subgraph Pre-Requisites
    subgraph Mandatory
      N/A
    end
    subgraph Optional
      gitleaks-toml>".gitleaks.toml"]
      commitlint-js>".commitlint.config.js"]
    end
  end
  subgraph Jobs
    subgraph Credentials / Secrets
      gitleaks{"GitLeaks"}
      stacs{"STACS"}
    end
    subgraph Commit Format
      commitlint{"Commit Lint"}
    end
  end
  subgraph Artifacts
    subgraph Commit Lint
      commit-lint-tty["TTY"]
    end
    subgraph Gitleaks
      gitleaks-tty["TTY"]
    end
    subgraph STACS
      stacs-tty["TTY"]
    end
  end

  %% dependencies -> Jobs
  gitleaks-toml-.->gitleaks
  commitlint-js-.->commitlint

  %% Jobs -> Artifacts
  commitlint--->commit-lint-tty
  gitleaks--->gitleaks-tty
  stacs--->stacs-tty
```

### Gitleaks

Runs Gitleaks which checks your repository for accidentally committed credentials

**Uses:** [zricethezav/gitleaks-action@v1.6.0](https://github.com/zricethezav/gitleaks-action)

### STACS

YARA powered static credential scanner which supports source code, binary file formats, analysis of 
nested archives, composable rule-sets and ignore lists

**Uses:** [stacscan/stacs-ci@0.1.1](https://github.com/stacscan/stacs-ci)

### Commit Lint

Scans the commit history to help your team adhere to a commit convention

**Uses:** [wagoid/commitlint-github-action@v4](https://github.com/wagoid/commitlint-github-action)

## Usage

Simply include the workflow within your project's workflow using something like the following.

```yaml
source-protection:
  uses: erzz/workflows/.github/workflows/source-protection.yml@main
```
## Secrets

| Output      | Description                                                   | Example value |
| ----------- | ------------------------------------------------------------- | ------------- |
| `short-sha` | Captures the short SHA for use in this or later workflow jobs | `cb26122`     |

## Inputs

?> You may want to tweak `fetch-depth` to a number that works for your projects. It determines how many commits to fetch for analysis in both the gitleaks and the commitlint jobs.
One option is to set to `0` which will fetch every commit but can be slow in long-lived repositories. It certainly should be reasonably many commits and definitely more than 10 to be usable
in the jobs

| Input                    | Required | Default                 | Details                                                                                                           |
| ------------------------ | -------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `fetch-depth`            | false    | `50`                    | How many commits to fetch from the repository. Set to 0 for all (slow!) - but at least a minimum of 2             |
| `creds-scan-directory`   | false    | `''`                    | Defaults to the repository root - specify your own path if required                                               |
| `creds-fail-build`       | false    | `true`                  | Defaults to failing the job if tests do not pass. Set to false for the opposite (yet not recommended!) behaviour" |
| `creds-gitleaks-config`  | false    | `.gitleaks.toml`        | Path to a custom gitleaks config if required                                                                      |
| `commits-enable`         | false    | `true`                  | Set to false if you want to disable the commit lint job                                                           |
| `commits-default-config` | false    | `true`                  | This workflow provides a commit lint config based on conventional commits. Set to false to use your own           |
| `commits-config-file`    | false    | `.commitlint.config.js` | Relative path to your own configuration for commit lint if not using the default                                  |
| `commits-fail-build`     | false    | `true`                  | Set to false if you do not want commit lint to fail on warnings                                                   |

## Outputs

| Output       | Description                                                   | Example value   |
| ------------ | ------------------------------------------------------------- | --------------- |
| `short-sha`  | Captures the short SHA for use in this or later workflow jobs | `cb26122`       |
| `ref-slug`   | A URL sanitized version of the github ref                     | `bug-mybranch1´ |

## Advanced Examples

### Run only the credential scanning jobs

Useful when running as part of a production deploy when there are no new commits.

```yaml
source-protection:
  uses: erzz/workflows/.github/workflows/source-protection.yml@main
  with:
    commits-enable: false
```


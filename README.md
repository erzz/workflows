# erzz / workflows

Reusable workflows for Github Actions

![erzz/workflows logo](docs/img/erzz-workflows-logo-large.png)

## Documentation

[Full documentation is here](https://erzz.github.io/workflows)

# Available Workflows

Below is a list of the available (and planned) workflows as I work through them.

The workflows themselves can be found under [.github/workflows](/.github/workflows). They MUST live there otherwise they cannot be called by other projects which is a shame - things would be more organised if Github allowed them to live under any path :(.

Please refer to the [Docs](https://erzz.github.io/workflows) for each workflow's usage instructions.

| Workflow                                                | Purpose                                   | Summary of jobs                                           | Docs                             |
| ---------------------                                   | ----------------------------------------- | --------------------------------------------------------- | -------------------------------- |
| [container](/.github/workflows/container.yml)           | Build, push and test container images     | Build & Push -> Hadolint & Dockle Lint & Trivy Image Scan | [Link](https://erzz.github.io/workflows/#/container/container)        |
| [container-oidc](/.github/workflows/container-oidc.yml) | As above but using OIDC authentication    | Build & Push -> Hadolint & Dockle Lint & Trivy Image Scan | [Link](https://erzz.github.io/workflows/#/container/container-oidc)        |
| [semantic-release](/.github/workflows/release.yml)      | Create releases based on semantic commits | Semantic-release using this repo's config or your own     | [Link](https://erzz.github.io/workflows/#/release/release) |
| [source-protection](/.github/workflows/source-protection.yml)      | Check commits for credentials and commit conventions | Gitleaks, STACS & CommitLint     | [Link](https://erzz.github.io/workflows/#/source-protection/source-protection) |
| node-tests                                              | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| go-tests                                                | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| java-tests                                              | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| deploy-cloud-run                                        | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| deploy-cloud-function                                   | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| terraform-tests                                         | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| terraform-apply                                         | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |

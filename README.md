# erzz / workflows

Reusable workflows for Github Actions

# Available Workflows

Below is a list of the available (and planned) workflows as I work through them.

The workflows themselves can be found under [.github/workflows](/.github/workflows). They MUST live there otherwise they cannot be called by other projects which is a shame - things would be more organised if Github allowed them to live under any path :(.

Docs for each workflow can be found under [docs](/docs).

For more information about re-usable workflows see https://docs.github.com/en/actions/learn-github-actions/reusing-workflows

| Workflow                                                | Purpose                                   | Summary of jobs                                           | Docs                             |
| ---------------------                                   | ----------------------------------------- | --------------------------------------------------------- | -------------------------------- |
| [container](/.github/workflows/container.yml)           | Build, push and test container images     | Build & Push -> Hadolint & Dockle Lint & Trivy Image Scan | [Link](docs/container.md)        |
| [container-oidc](/.github/workflows/container-oidc.yml) | As above but using OIDC authentication    | Build & Push -> Hadolint & Dockle Lint & Trivy Image Scan | [Link](docs/container.md)        |
| [semantic-release](/.github/workflows/release.yml)      | Create releases based on semantic commits | Semantic-release using this repo's config or your own     | [Link](docs/semantic-release.md) |
| node-tests                                              | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| go-tests                                                | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| java-tests                                              | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| deploy-cloud-run                                        | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| deploy-cloud-function                                   | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| terraform-tests                                         | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |
| terraform-apply                                         | Coming Soon                               | Coming Soon                                               | [Link](docs/container.md)        |

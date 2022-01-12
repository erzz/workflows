# Container (OIDC) Workflow

## Basic

There are two alternative workflows (due to numerous actions limitations) depending on which type of authentication you use between Github Actions and GCP. If you want to use Basic or Service Account authentication then see [container.yml](/container/container.md)

**Using OIDC Authentication**

```yaml
build:
  uses: erzz/workflows/.github/workflows/container-oidc.yml@main
  with:
    registry: "eu.gcr.io"
    image: image-path/image-name
  secrets:
    wip: projects/012345678901/locations/global/workloadIdentityPools/github/providers/github
    service-account: my-service-account@my-project.iam.gserviceaccount.com
```

!> Ensure that you have actually set up and configured OIDC authentication between Github and GCP first!

## Secrets

| Input               | Required     | Details                                                                                                 |
| ------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| `wip`               | true         | The workload identity provider to use with the **container-oidc.yml** workflow                          |
| `service-account`   | true         | The service account to impersonate when using the **container-oidc.yml** workflow                       |
| `npm-token`         | false        | If using a private NPM registry, provide the token and it will be exported as NPM_TOKEN in the workflow |
| `mvn-settings-file` | false        | If a maven settings file is required provide the secret containing the file                             |

## Inputs

| Input             | Required | Default        | Details                                                                                            |
| ----------------- | -------- | -------------- | -------------------------------------------------------------------------------------------------- |
| `image`           | true     | N/A - REQUIRED | The path and image name to create e.g. `my-project/myapp` Note: tags will be automatically created |
| `registry`        | false    | `eu.gcr.io`    | The domain name of the registry to push the built image to                                         |
| `dockerfile`      | false    | `Dockerfile`   | Relative path to the Dockerfile to build from                                                      |
| `build-args`      | false    | N/A            | Comma separated list of environment variables to pass as build args                                |
| `env-file`        | false    | `false`        | If there is an `.env` file to include set to true - expects an artifact named env-file             |
| `mvn-settings`    | false    | `false`        | Set to true in combination with the mvn-settings-file secret if a maven settings file is required  |
| `trivy-scan-type` | false    | `os,library`   | The comma separated list of the scan types to perform (no spaces!)                                 |
| `include-tests`   | false    | `true`         | Set to false in order to skip the tests and only run the build & push job                          |

## Outputs

| Output       | Description                                     | Example value                 |
| ------------ | ----------------------------------------------- | ----------------------------- |
| `image-name` | The full registry and path of the built image   | `eu.gcr.io/my-project/my-app` |
| `image-tag`  | The image tag applied to the built image        | `main-23f1a`                  |
| `branch`     | The branch or tag for which the image was built | `main`                        |

## Adavnced Examples

### Custom Dockerfile location

```yaml
build:
  needs: [env-file]
  uses: erzz/workflows/.github/workflows/container.yml@main
  with:
    image: my-project/my-app
    dockerfile: build/Dockerfile
  secrets:
    wip: projects/012345678901/locations/global/workloadIdentityPools/github/providers/github
    service-account: my-service-account@my-project.iam.gserviceaccount.com
```

### NodeJS with private NPM Registry & .env file

```yaml
build:
  needs: [env-file]
  uses: erzz/workflows/.github/workflows/container.yml@main
  with:
    registry: "eu.gcr.io"
    image: my-project/my-app
    build-args: NPM_TOKEN
    env-file: true
    trivy-scan-type: "os"
  secrets:
    wip: projects/012345678901/locations/global/workloadIdentityPools/github/providers/github
    service-account: my-service-account@my-project.iam.gserviceaccount.com
    npm-token: ${{ secrets.ARTIFACTORY_AUTH_TOKEN }}
```

### Go using .env file and skipping the test jobs

```yaml
build:
  needs: [env-file]
  uses: erzz/workflows/.github/workflows/container.yml@main
  with:
    image: my-project/my-app
    env-file: true
    include-tests: false
  secrets:
    wip: projects/012345678901/locations/global/workloadIdentityPools/github/providers/github
    service-account: my-service-account@my-project.iam.gserviceaccount.com
```

### Maven with maven-settings.xml

```yaml
jobs:
  build:
    uses: erzz/workflows/.github/workflows/container.yml@main
    with:
      image: my-project/my-app
      mvn-settings: true
    secrets:
      wip: projects/012345678901/locations/global/workloadIdentityPools/github/providers/github
      service-account: my-service-account@my-project.iam.gserviceaccount.com
      mvn-settings-file: ${{ secrets.MAVEN_SETTINGS_FILE }}
```
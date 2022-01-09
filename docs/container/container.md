# Container (Basic Auth) Workflow

## Usage

There are two alternative workflows (due to numerous actions limitations) depending on which type of authentication you use between Github Actions and GCP. If you want to use OIDC authentication then see [container-oidc.yml](/container/container-oidc.md)

**Using Service Account Key**

```yaml
build:
  uses: erzz/workflows/.github/workflows/container.yml@main
  with:
    registry: "eu.gcr.io"
    image: image-path/image-name
  secrets:
    user: _json_key
    password: ${{ secrets.SA_JSON }}
```

## Secrets

| Input               | Required | Details                                                                                                |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `user`              | true     | Username to use for authenticating with your target registry when using the **container.yml** workflow |
| `password`          | true     | Password to use for authenticating with your target registry when using the **container.yml** workflow |
| `npm-token`         | false    | If using a private NPM repo, provide the token and it will be exported as NPM_TOKEN in the workflow    |
| `mvn-settings-file` | false    | If a maven settings file is required provide the secret containing the file                            |

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

## Other Examples

### Using a Dockerfile that is not at repository root

```yaml
build:
  needs: [env-file]
  uses: erzz/workflows/.github/workflows/container.yml@main
  with:
    image: my-project/my-app
    dockerfile: build/Dockerfile
  secrets:
    user: _json_key
    password: ${{ secrets.SA_JSON_KEY }}
```

### NodeJS container using private NPM registry plus a .env file from previous job

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
    user: _json_key
    password: ${{ secrets.SA_JSON_KEY }}
    npm-token: ${{ secrets.ARTIFACTORY_AUTH_TOKEN }}
```

### Go container using .env file from previous job and skipping the test jobs

```yaml
build:
  needs: [env-file]
  uses: erzz/workflows/.github/workflows/container.yml@main
  with:
    image: my-project/my-app
    env-file: true
    include-tests: false
  secrets:
    user: _json_key
    password: ${{ secrets.SA_JSON_KEY }}
```

### Maven-built Java container using a maven-settings.xml file

```yaml
jobs:
  build:
    uses: erzz/workflows/.github/workflows/container.yml@main
    with:
      image: my-project/my-app
      mvn-settings: true
    secrets:
      user: _json_key
      password: ${{ secrets.SA_JSON_KEY }}
      mvn-settings-file: ${{ secrets.MAVEN_SETTINGS_FILE }}
```
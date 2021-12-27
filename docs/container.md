# Container Worflow

![Container Workflow](/media/container.png)

This workflow will:

- Build your container image (uses [mr-smithers-excellent/docker-build-push@v5](https://github.com/mr-smithers-excellent/docker-build-push))
- Automatic git-ops-like tags (uses [mr-smithers-excellent/docker-build-push@v5](https://github.com/mr-smithers-excellent/docker-build-push))
- Push to a registry of your choice (uses [mr-smithers-excellent/docker-build-push@v5](https://github.com/mr-smithers-excellent/docker-build-push))
- Scan image with Trivy for dependency and OS vulnerabilites (uses [aquasecurity/trivy-action@master](https://github.com/aquasecurity/trivy-action))
- Lint the Dockerfile with Hadolint (uses [hadolint/hadolint-action@v1.6.0](https://github.com/hadolint/hadolint-action))
- Test against best practices using Dockle (uses [erzz/dockle-action@v1.1.1](https://github.com/erzz/dockle-action))

# Usage

Simply include the workflow within your project's workflow using something like

```yaml
build:
  uses: erzz/workflows/.github/workflows/container.yml@v1
  with:
    registry: "eu.gcr.io"
    image: image-path/image-name
  secrets:
    user: _json_key
    password: ${{ secrets.SA_JSON }}
```

# Secrets

| Input               | Required | Default        | Details                                                                                             |
| ------------------- | -------- | -------------- | --------------------------------------------------------------------------------------------------- |
| `user`              | true     | N/A - REQUIRED | Username to use for authenticating with your target registry                                        |
| `password`          | true     | N/A - REQUIRED | Password to use for authenticating with your target registry                                        |
| `npm-token`         | false    | N/A            | If using a private NPM repo, provide the token and it will be exported as NPM_TOKEN in the workflow |
| `mvn-settings-file` | false    | N/A            | If a maven settings file is required, provide the secret and it will be created in the workflow     |

# Inputs

| Input             | Required | Default        | Details                                                                                            |
| ----------------- | -------- | -------------- | -------------------------------------------------------------------------------------------------- |
| `image`           | true     | N/A - REQUIRED | The path and image name to create e.g. `my-project/myapp` Note: tags will be automatically created |
| `registry`        | false    | `eu.gcr.io`    | The domain name of the registry to push the built image to                                         |
| `build-args`      | false    | N/A            | Comma separated list of environment variables to pass as build args                                |
| `env-file`        | false    | `false`        | If there is an `.env` file to include set to true - expects an artifact named env-file             |
| `trivy-scan-type` | false    | `os,library`   | The comma separated list of the scan types to perform (no spaces!)                                 |
| `include-tests`   | false    | `true`         | Set to false in order to skip the tests and only run the build & push job                          |

# Outputs

| Output     | Description                                     | Example value                 |
| ---------- | ----------------------------------------------- | ----------------------------- |
| image-name | The full registry and path of the built image   | `eu.gcr.io/my-project/my-app` |
| image-tag  | The image tag applied to the built image        | `main-23f1a`                  |
| branch     | The branch or tag for which the image was built | `main`                        |

# Examples

## NodeJS container using private NPM registry plus a .env file from previous job

```yaml
build:
  needs: [env-file]
  uses: erzz/workflows/.github/workflows/container.yml@v1
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

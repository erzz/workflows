## [1.3.0](https://github.com/erzz/workflows/compare/v1.2.0...v1.3.0) (2022-01-05)


### :package: Maintenance

* **deps:** update rlespinasse/github-slug-action action to v4 ([196827c](https://github.com/erzz/workflows/commit/196827c02f1e21949e05653ed4250590854ff073))


### :bug: Bug Fixes

* re-add oidc credentials ([28860f1](https://github.com/erzz/workflows/commit/28860f1c2b56abe6dd23f0e620676b60573d930b))


### :sparkles: New Features

* add credential scanning and commit linting ([3f67060](https://github.com/erzz/workflows/commit/3f670603a7253f804a2d78b2dd21d9ccc1ed374f))
* add option to disable commit lint if required ([595d2a8](https://github.com/erzz/workflows/commit/595d2a872d16fdc9d56e7bbb9c95583e943b6893))

## [1.2.0](https://github.com/erzz/workflows/compare/v1.1.0...v1.2.0) (2022-01-01)


### :bug: Bug Fixes

* add chore: as releasable for maven projects ([1676dee](https://github.com/erzz/workflows/commit/1676deeca12fd73949490eee5bdd634d3ed09d78))
* **semantic-release:** handle the maven case with settings file ([1305e4e](https://github.com/erzz/workflows/commit/1305e4e91324978b8f0ecf414788ec58c318c04e))


### :sparkles: New Features

* **container:** add support for custom Dockerfile location ([e1dc3f6](https://github.com/erzz/workflows/commit/e1dc3f6d89ae35791030ccad72c5d457d385d51b))
* **container:** provide oidc version of container workflow ([bbca16e](https://github.com/erzz/workflows/commit/bbca16efcc0ffffb59036ec1dcae805424749d81))

## [1.1.0](https://github.com/erzz/workflows/compare/v1.0.1...v1.1.0) (2021-12-28)


### :sparkles: New Features

* add a semantic release workflow with option to use default configuration ([79a97c4](https://github.com/erzz/workflows/commit/79a97c468e1869cb6f1f3340a723eea525726f31))


### :bug: Bug Fixes

* **release:** remove required for inputs.default-config as default is provided ([e23d407](https://github.com/erzz/workflows/commit/e23d407a85b5913991beebb35d5edc00c88db329))

## [1.0.1](https://github.com/erzz/workflows/compare/v1.0.0...v1.0.1) (2021-12-27)


### Bug Fixes

* add handling of maven-settings.xml file for maven projects ([afab263](https://github.com/erzz/workflows/commit/afab263186d09b8ea6ba80f95f69e24176c478f9))

# 1.0.0 (2021-12-23)


### Features

* add trivy image scanning for deps and os ([1fb3f22](https://github.com/erzz/workflows/commit/1fb3f2270f3ea3b693e271e6542423160b345965))
* build and push images to target registry ([6bcf5d8](https://github.com/erzz/workflows/commit/6bcf5d8744c4d46c5371f086702fdfbfc171b3ad))
* handle env file case when required ([b545ce0](https://github.com/erzz/workflows/commit/b545ce002946e1dc649d86ec9852f7af132e70cf))
* option to disable tests and only run build & push ([3d3609b](https://github.com/erzz/workflows/commit/3d3609b8e554b6a3746ecf35616f9b0e5d7f7d58))
* outputs for image, tag and branch ([0074d27](https://github.com/erzz/workflows/commit/0074d27807442783b29ed3a2f5d0f6036cd55bc7))
* scan images with Dockle and Hadolint ([48ce22f](https://github.com/erzz/workflows/commit/48ce22ffa0b4b6c84de54fb63c440cfd906f0ebd))
* support NPM_TOKEN ([6d0494c](https://github.com/erzz/workflows/commit/6d0494c0f196795f8069084b2e304d5ee452538a))

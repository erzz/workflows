## [1.6.0](https://github.com/erzz/workflows/compare/v1.5.0...v1.6.0) (2022-01-17)


### :sparkles: New Features

* **tf-tests:** add lint, validate, plan and tfsec jobs ([d40b9c4](https://github.com/erzz/workflows/commit/d40b9c4a7b38832a8cb04cb16aa581f9eebfa1c2))


### :bug: Bug Fixes

* **tf-plan:** pass vars as secret as may contain secret values ([8997d95](https://github.com/erzz/workflows/commit/8997d9594f3a9a5994fda6c0f20258a88243606e))

## [1.5.0](https://github.com/erzz/workflows/compare/v1.4.0...v1.5.0) (2022-01-13)


### :bug: Bug Fixes

* **eslint:** correct the report path ([ec9ca1c](https://github.com/erzz/workflows/commit/ec9ca1c5ead5200423192e6bd52718b7c3944cc3))
* **general:** update workflow names ([ed831fd](https://github.com/erzz/workflows/commit/ed831fd065de756e22f784e6b531b5fd71574cdc))


### :package: Maintenance

* **deps:** update rlespinasse/github-slug-action action to v4 ([1338bd5](https://github.com/erzz/workflows/commit/1338bd5538b22fdb4ce0a829016a8f6c03d0b070))
* **deps:** update stacscan/stacs-ci action to v0.1.4 ([e1bd1fa](https://github.com/erzz/workflows/commit/e1bd1fa7dd4ed7fb610a7d1adf7984bf92a38c7f))
* **java-tests:** remove extra character in input description ([12866e4](https://github.com/erzz/workflows/commit/12866e4a3ae6db2d60517d3784ad45e28c87642f))


### :sparkles: New Features

* add node-tests workflow ([1b9fe01](https://github.com/erzz/workflows/commit/1b9fe01627ff860bae31549a6ed368ec59c22ce1))
* **go-tests:** add gosec, unit tests and code-quality ([729f866](https://github.com/erzz/workflows/commit/729f8667e0dca30750aa62ff7e89d368bc321f42))
* **go-tests:** add option for GCP auth in unit tests ([5b70399](https://github.com/erzz/workflows/commit/5b703993aa6cfd86a9a78eaf1a4c0f1c1351427c))
* **gosec:** add option to pass extra flags ([5b15ea3](https://github.com/erzz/workflows/commit/5b15ea339ddf98abc621e0f7c64c39b209001f53))
* **njsscan:** add option to provide your own config ([1d3157c](https://github.com/erzz/workflows/commit/1d3157c16aebe0664377f343777c1800134433a7))
* **node-tests:** add switches to enable/disable each job ([63a40c6](https://github.com/erzz/workflows/commit/63a40c66d4db2dcb72164ba750f864d96ffe9334))

## [1.4.0](https://github.com/erzz/workflows/compare/v1.3.0...v1.4.0) (2022-01-10)


### :sparkles: New Features

* **java-tests:** add code quality job ([215a032](https://github.com/erzz/workflows/commit/215a032504abf61154e52794ce462e6770b349f5))
* **java-tests:** add polaris SAST scanning ([07634b5](https://github.com/erzz/workflows/commit/07634b562313dd95d5010a339580544dd3897cf4))
* **java-tests:** add unit-test job ([21e95bd](https://github.com/erzz/workflows/commit/21e95bdb23a3221e118de3f22b9a146dbcbfe5bd))
* **polaris:** provide polaris result analyzer ([d6de55e](https://github.com/erzz/workflows/commit/d6de55e6d2803fd75b60fbb7eefee4de2bd03e59))


### :package: Maintenance

* **deps:** update stacscan/stacs-ci action to v0.1.2 ([5248ec5](https://github.com/erzz/workflows/commit/5248ec54e12d473c7d9b0ac6f91771b3f45464ae))


### :bug: Bug Fixes

* **commit-lint:** provide conventional config as baseline with reasonable fetch depth ([b7948c5](https://github.com/erzz/workflows/commit/b7948c5fa00dd1135da25ce3b5af40ff010c9ac6))
* make failure more robust when fetching configs ([b4a2f81](https://github.com/erzz/workflows/commit/b4a2f81e169293c8737703c3653bd1d8b584aa1b))
* **polaris:** add fetching of the polaris.yml config ([c7817ef](https://github.com/erzz/workflows/commit/c7817efa273b329f505538edfbc6639ef71a840c))
* **polaris:** fetch the result analyzer as part of the job ([f12dd66](https://github.com/erzz/workflows/commit/f12dd6646f28befaabcc626b716e176438e8d8e2))
* **polaris:** remove prefix from project name ([30d61d1](https://github.com/erzz/workflows/commit/30d61d11d9908858a34e1c49c107287d389ba966))
* **unit-tests:** fix broken images in jacoco report ([4393362](https://github.com/erzz/workflows/commit/4393362c72668480fcc53c9391f11a80cc925dd3))
* **unit-tests:** remove duplicate upload of surefire reports ([75288e5](https://github.com/erzz/workflows/commit/75288e550d7c02c56f8cc53de36c2745d9edd95b))

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

# Node-Tests Workflow Overview

## Purpose

This workflow will execute tests on your NodeJS application that require only the code (i.e. no deployed environment) using typical yarn or npm commands.

In general it will run Unit Tests, ESLint and NJSScan for the build.

!> The workflow itself will not provide the scripts and dependencies. It simply executes your commands and provide artifacts if the appropriate dependencies are installed and configured

- General
  - Configurable NodeJS version
  - All relevant jobs have the option to provide an NPM_TOKEN for authentication with private repositories
- ESLint
  - Provides HTML report if configured
- NJS Scan (SAST)
  - Provides a default configuration with the option to use your own
  - Provides an HTML report as an artifact
- Unit Tests
  - Provides HTML report and Code Coverage if configured

## Included Jobs

```mermaid
%%{init: {'theme': 'neutral'}}%%

flowchart LR
  subgraph Pre-Requisites
    subgraph Mandatory
      eslint-package>"ESLint\n(NPM/Yarn)"]
      jest-package>"Jest\n(NPM/Yarn)"]
    end
    subgraph Optional
      npm-token>"NPM_TOKEN\n(Secret)"]
    end
  end
  subgraph Jobs
    code-quality{"ESLint"}
    unit-tests{"Custom\nUnit Tests"}
    sast{"NJSScan"}
  end
  subgraph Artifacts
    subgraph ESLint
      es-html["eslint-report.html"]
    end
    subgraph Unit Tests & Coverage
      test-report-html["test-report.html"]
      junit-xml["junit.xml"]
      cobertura-xml["cobertura-coverage.xml"]
    end
    subgraph SAST
      njsscan-html["njsscan.html"]
    end
  end

  %% dependencies -> Jobs
  eslint-package-->code-quality
  jest-package-->unit-tests
  npm-token-.->code-quality
  npm-token-.->unit-tests
  
  %% Jobs -> Artifacts
  code-quality-->es-html
  sast-->njsscan-html
  unit-tests-->test-report-html
  unit-tests-->junit-xml
  unit-tests-->cobertura-xml
```

### ESLint

Runs an install and test script of your choice with the default being `yarn lint:ci`

**Uses:** N/A Your own NodeJS Scripts

### NJSScan

NJSScan is a static application testing (SAST) tool that can find insecure code patterns in your node.js applications using simple pattern matcher from libsast and syntax-aware semantic code pattern search tool semgrep.

**Uses:** [ajinabraham/njsscan-action@master](https://github.com/ajinabraham/njsscan-action)


### Unit Tests

Runs an install and test script of your choice with the default being `yarn test:unit-ci`

**Uses:** N/A Your own NodeJS Scripts
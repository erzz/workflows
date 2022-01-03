---
title: "Semantic Release Workflow"
weight: 1
---

## Purpose

This workflow will:

- Analyze your semantic commit git history, and create a semantically versioned release if required
- Provides a [standard configuration](/.github/workflows/semantic-release-config.json) with option to disable and use the config already in your repository.
- Options to switch to [maven version](/.github/workflows/semantic-release-config-mvn.json) of the semantic-release configuration which also updates the version in pom.xml
- Option for a maven-settings.xml file to be created from a secret

## Jobs

{{< mermaid >}}
%%{init: {'theme': 'dark'}}%%
flowchart LR
  subgraph release
    semantic-release["Run Semantic Release"]
  end
{{< /mermaid >}}

### Run Semantic Release

Uses: [cycjimmy/semantic-release-action@v2.7.0](https://github.com/cycjimmy/semantic-release-action)

Runs Semantic Release to analyse commit history and decide on whether a release should be created. If a release is created it takes care of semantic versioning, release notes, CHANGELOG.md etc

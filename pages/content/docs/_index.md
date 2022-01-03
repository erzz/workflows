---
title: "Basics"
weight: 1
---

Reusable workflows are called with a simple syntax and may expose both `inputs` (options to pass) and `secrets` (credentials and protected values).

- Provide inputs using the `with:` context
- Provide secrets with the `secrets:` context
- Optionally pin the version used e.g. `@v1.2.0` or be brave and pin to `@main` branch which may be less reliable!

{{< tip >}}
Check each workflow's docs to see which inputs and secrets you must provide either as mandatory or optional values.
{{< /tip >}}

To include a workflow - simply add it to any workflow in your current repository with the following pattern of usage.

```yaml
jobs:
  give-me-a-name:
    uses: erzz/workflows/.github/workflows/reusable-workflow.yml@main
    with:
      input1: value1
      input2: value2
    secrets:
      some-secret: ${{ secrets.SOME_SECRET }}
```

For more information and official docs see https://docs.github.com/en/actions/learn-github-actions/reusing-workflows#calling-a-reusable-workflow

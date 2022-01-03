+++
title = "erzz/workflows"
[data]
baseChartOn = 3
colors = ["#627c62", "#11819b", "#ef7f1a", "#4e1154"]
columnTitles = ["Section", "Status", "Author"]
fileLink = "content/projects.csv"
title = "Projects"

+++
{{< block "grid-2" >}}
{{< column >}}

# Reusable workflows for Github Actions

Instead of copy & pasting a ton of workflow files and tweaking for each project, using reusable workflows has numerous advantages:

- Less CI & CD code to maintain!
- Apply a single change across many projects instead of dozens of PR's
- Consistency in knowing that all projects are built and tested in the same way
- Get up and running with new projects much faster!

{{< tip >}}
Feel free to open a [PR](https://github.com/erzz/workflows/pulls), raise an [issue](https://github.com/erzz/workflows/issues "Open a Github Issue") or request a new feature / workflow.
{{< /tip >}}

{{< tip "warning">}}
As of January 2022, this project is still a work in progress! There will be many updates, fixes and changes whilst the project takes shape. So it is **HIGHLY** recommended that you pin the version of workflows you use for stability.

To get updates to your workflows in a more controlled way, I highly recommend setting up [Renovate](https://github.com/renovatebot/renovate) and you will receive a PR automatically as new versions are released.
{{< /tip >}}

{{< button "docs/" "Read the Docs" >}}{{< button "https://github.com/erzz/workflows" "Go to the source" >}}
{{< /column >}}

{{< column >}}
![diy](/images/workflows.png)
{{< /column >}}
{{< /block >}}
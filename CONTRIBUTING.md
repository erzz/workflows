# Contributing

All contributions are welcome via a Pull Request either from a branch of this repository or your own fork.

Creation of a Pull Request does not mean it will be accepted! Please don't take it personally if a PR is 
rejected or changes are requested! Even PR's that are rejected contribute to the pool of ideas and 
requirements floating around and it can be a matter of personal preference in the end. 

This project is rather opinionated in the end and that's because its used heavily in my own day job. 
But its an MIT license - so fork, copy, whatever for your own personal needs.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build. Add to the .gitignore if required!
2. Update the `docs/` with details of any changes, this includes new inputs, 
   secrets, variables, useful file locations and container parameters.
3. All commit messages must follow the [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/)
   format!
4. Only project memebers can merge a Pull Request after at least one approval.

## Working with the Docs

The docs are built using [Docsify](https://docsify.js.org/) which is a very simple markdown based system.

To build and test docs locally before commit simply run the following to have a local server up and running:

```bash
npm i docsify-cli -g
docsify serve docs
```

You will now be able to see realtime updates to the look and feel of the docs as you work with them at
http://localhost:3000

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
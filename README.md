# SSS TODO-track-name

This is the private (internal) repository for the **TODO-track-name** track of the Security Summer School (SSS).
It contains deployment files and scripts, source code files for activities and CTF challenges.
This is to be used internally by members of the SSS **TODO-track-name** team for content development.
It can be made available to partners who want to use the content for their own class / event.

Public content is available to students, participants and hobbyists in the [public repository pair](https://github.com/security-summer-school/template-public/) (TODO: fix link).

## Developing Content

Content is to be developed both in this private (internal) repository and in the [public repository pair](https://github.com/security-summer-school/template-public/) (TODO: fix link).
See the [contribution guide](CONTRIBUTING.md) on how you could report or fix issues and on how you can improve content.

Reviewers are requested to follow the [reviewing guide](REVIEWING.md).

For in-depth discussions, please join the [SSS Discord community](https://discord.gg/qx3RmNEVkB).

## CTF Challenges

CTF (_Capture the Flag_) challenges are only located in this private repository.
These are challenges that are to be solved by participants in simulated contests.
Participants will only be provided with a link to a CTF platform that hosts challenges: description, support files, form for submitting the flag.

The `ctf/` folder stores CTF challenges.
There are typically two CTFs: a `final-ctf` and a `mid-ctf`.
Each challenge has its own folder.

### CTF Challenge Folder Structure

A CTF challenge folder consists of:

- `README.md`: details the challenge name, challenge description, points, hints, vulnerability overview, solution overview, deployment instructions.
- `flag`: contains the flag string.
- `sol/`: stores the reference solution scripts (`solution.py`, `solution.sh`, `solution.c` + `Makefile` or others).
- `src/` (optional): stores source code and build scripts to generate deployment or public files.
  To keep things generic, flags shouldn't be hard-coded in source code files.
  The recommended way is to use a template file and then use a generator script (using `sed` or something similar) that generates the actual file (with the flag inside).
  Most challenges require a source code folder, but some may not, making the `src/` folder optional.
- `public/` (optional): stores public files that are to be packed in an archive that is to be made available to participants.
  They are usually generated from the `src/` folder, though they may also be static files.
  Some challenges may not have any public archive to be presented to contestants, making the `public/` folder optional.
- `deploy/` (optional): stores deployment files, to be used to host the challenge on a remote system to be exploited by participants, typically in the form of a Docker container.
  Most challenges require remote deployment in a Docker container, but some may not, making the `deploy/` folder optional.

  It typically consists of the following files:

  - `Dockerfile`: for creating the Docker container that will run the challenge on the remote system.
  - `docker-compose.yml`: for configuring the Docker containers
  - `.dockerignore`: for [excluding](https://docs.docker.com/engine/reference/builder/#dockerignore-file) some files from the Docker container.
  - `Makefile`: the building and running of Docker containers.
    This file should include `common/challenge.mk` in most cases, but if a challenge has a different structure it can implement its own Makefile.
  - `run.sh` (when required): Docker startup script, used to start services.
    It's used inside the `Dockerfile` with `COPY + CMD` commands.
  - Additional files required for the deployment.
    They may be static files or files generated from the `src/` folder.

  Content already part of the `public/` folder, required in `Dockerfile`, `run.sh` or other scripts, won't be duplicated in the `deploy/` folder.
  It will be used directly from the `public/` folder.

The `ctf/ctf-1/challenge-folder-1/` folder contains scaffolding contents of a CTF challenge folder:

```
|-- deploy/
|   |-- .dockerignore (optional)
|   |-- docker-compose.yml
|   |-- Dockerfile
|   |-- Makefile
|   `-- run.sh
|-- flag
|-- public/
|-- README.md
|-- sol/
|   |-- README.md
|   |-- solution.py
|   `-- solution.sh*
`-- src/
    `-- index.template.php
```

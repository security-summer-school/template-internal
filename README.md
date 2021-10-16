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

CTF (*Capture the Flag*) challenges are only located in this private repository.
These are challenges that are to be solved by participants in simulated contests.
Participants will only be provided with a link to a CTF platform that hosts challenges: description, support files, form for submitting the flag.

The `ctf/` folder stores CTF challenges.
There are typically two CTFs: a `final-ctf` and a `mid-ctf`.
Each challenge has its own folder.

### CTF Challenge Folder Structure

A CTF challenge folder consists of:

* `README.md`: details the challenge name, challenge description, points, hints, vulnerability overview, solution overview, deployment instructions.
* `flag`: contains the flag string.
* `sol/`: stores the reference solution scripts (`solution.py`, `solution.sh`, `solution.c` + `Makefile` or others), and a solution write-up (a detailed set of steps) in `README.md`.
* `src/` (optional): stores source code and build scripts to generate deployment or public files.
  To keep things generic, flags shouldn't be hard-coded in source code files.
  The recommended way is to use a template file and then use a generator script (using `sed` or something similar) that generates the actual file (with the flag inside).

  Most challenges require a source code folder, but some may not, making the `src/` folder optional.
* `public/` (optional): stores public files that are to be packed in an archive that is to be made available to participants.
  They are usually generated from the `src/` folder, though they may also be static files.

  Some challenges may not have any public archive to be presented to contestants, making the `public/` folder optional.
* `deploy/` (optional): stores deployment files, to be used to host the challenge on a remote system to be exploited by participants, typically in the form of a Docker container.

  Most challenges require remote deployment in a Docker container, but some may not, making the `deploy/` folder optional.

  It typically consists of the following files:

  * `Dockerfile`: for creating the Docker container that will run the challenge on the remote system.
  * `docker-compose.yml` / `Makefile`: for configuring the building and running of the Docker containers
  * `run.sh` (when required): Docker startup script, used to start services.
    It's used inside the `Dockerfile` with `COPY + CMD` commands.
  * Additional files required for the deployment.
    They may be static files or files generated from the `src/` folder.

  Content already part of the `public/` folder, required in `Dockerfile`, `run.sh` or other scripts, won't be duplicated in the `deploy/` folder.
  It will be used directly from the `public/` folder.

## Sessions

As with all SSS tracks, the **TODO-track-name** track consists of multiple sessions.
One session typically covers a particular topic of the track.
Session contents are split among the private and the public repository.

In a private repository, a session folder contains a set of activity folders.
Activities come in two forms:

* **tutorials**: that provide a step-by-step detailing of the solution.
* **challenges**: that only state the goal and provide an initial skeleton (and maybe some hints), then the rest is up to participants.
  Even so, public challenge activity folders store the reference solution to help participants in case they're lost.

### Activity Folder Structure

An activity folder has a similar structure to the [CTF Challenge Folder Structure](#ctf-challenge-folder-structure), as shown below:

* `README.md`: stores similar contents to a CTF challenge.
* `flag` (optional): contains the flag string.
  Some activities may not have a flag, making it optional.
* `sol/`: stores the solution write-up (a detailed set of steps) in `README.md` for challenge activities only.
  The `README.md` for tutorial activities is stored in the corresponding folder in the public repository.
  Solution scripts are stored in the public repository.
* `src/` (optional): stores similar contents to a CTF challenge.
  The generated files that are to be made available to participants will be stored in the `public/` folder in the corresponding activity folder in the public repository.

  Most activities require a source code folder, but some may not, making the `src/` folder optional.
* `deploy/` (optional): stores similar contents to a CTF challenge.

  Most activities require remote deployment in a Docker container, but some may not, making the `deploy` folder optional.

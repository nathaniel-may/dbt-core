# Contributing to `dbt`

1. [About this document](#about-this-document)
2. [Proposing a change](#proposing-a-change)
3. [Getting the code](#getting-the-code)
4. [Setting up an environment](#setting-up-an-environment)
5. [Running `dbt` in development](#running-dbt-in-development)
6. [Testing](#testing)
7. [Submitting a Pull Request](#submitting-a-pull-request)

## About this document

This document is a guide intended for folks interested in contributing to `dbt-core`. Below, we document the process by which members of the community should create issues and submit pull requests (PRs) in this repository. It is not intended as a guide for using `dbt-core`, and it assumes a certain level of familiarity with Python concepts such as virtualenvs, `pip`, python modules, filesystems, and so on. This guide assumes you are using macOS or Linux and are comfortable with the command line.

If you're new to python development or contributing to open-source software, we encourage you to read this document from start to finish. If you get stuck, drop us a line in the `#dbt-core-development` channel on [slack](https://community.getdbt.com).

#### Adapters

If you have an issue or code change suggestion related to a specific database [adapter](https://docs.getdbt.com/docs/available-adapters); please refer to that supported databases seperate repo for those contributions.

### Signing the CLA

Please note that all contributors to `dbt-core` must sign the [Contributor License Agreement](https://docs.getdbt.com/docs/contributor-license-agreements) to have their Pull Request merged into the `dbt-core` codebase. If you are unable to sign the CLA, then the `dbt-core` maintainers will unfortunately be unable to merge your Pull Request. You are, however, welcome to open issues and comment on existing ones.

## Proposing a change

`dbt-core` is Apache 2.0-licensed open source software. `dbt-core` is what it is today because community members like you have opened issues, provided feedback, and contributed to the knowledge loop for the entire communtiy. Whether you are a seasoned open source contributor or a first-time committer, we welcome and encourage you to contribute code, documentation, ideas, or problem statements to this project.

### Defining the problem

If you have an idea for a new feature or if you've discovered a bug in `dbt-core`, the first step is to open an issue. Please check the list of [open issues](https://github.com/dbt-labs/dbt-core/issues) before creating a new one. If you find a relevant issue, please add a comment to the open issue instead of creating a new one. There are hundreds of open issues in this repository and it can be hard to know where to look for a relevant open issue. **The `dbt-core` maintainers are always happy to point contributors in the right direction**, so please err on the side of documenting your idea in a new issue if you are unsure where a problem statement belongs.

> **Note:** All community-contributed Pull Requests _must_ be associated with an open issue. If you submit a Pull Request that does not pertain to an open issue, you will be asked to create an issue describing the problem before the Pull Request can be reviewed.

### Discussing the idea

After you open an issue, a `dbt-core` maintainer will follow up by commenting on your issue (usually within 1-3 days) to explore your idea further and advise on how to implement the suggested changes. In many cases, community members will chime in with their own thoughts on the problem statement. If you as the issue creator are interested in submitting a Pull Request to address the issue, you should indicate this in the body of the issue. The `dbt-core` maintainers are _always_ happy to help contributors with the implementation of fixes and features, so please also indicate if there's anything you're unsure about or could use guidance around in the issue.

### Submitting a change

If an issue is appropriately well scoped and describes a beneficial change to the `dbt-core` codebase, then anyone may submit a Pull Request to implement the functionality described in the issue. See the sections below on how to do this.

The `dbt-core` maintainers will add a `good first issue` label if an issue is suitable for a first-time contributor. This label often means that the required code change is small, limited to one database adapter, or a net-new addition that does not impact existing functionality. You can see the list of currently open issues on the [Contribute](https://github.com/dbt-labs/dbt-core/contribute) page.

Here's a good workflow:
- Comment on the open issue, expressing your interest in contributing the required code change
- Outline your planned implementation. If you want help getting started, ask!
- Follow the steps outlined below to develop locally. Once you have opened a PR, one of the `dbt-core` maintainers will work with you to review your code.
- Add a test! Tests are crucial for both fixes and new features alike. We want to make sure that code works as intended, and that it avoids any bugs  previously encountered. Currently, the best resource for understanding `dbt-core`'s [unit](test/unit) and [integration](test/integration) tests is the tests themselves. One of the maintainers can help by pointing out relevant examples.
- Check your formatting and linting with [Flake8](https://flake8.pycqa.org/en/latest/#), [Black](https://github.com/psf/black), and the rest of the hooks we have in our [pre-commit](https://pre-commit.com/) [config](https://github.com/dbt-labs/dbt-core/blob/75201be9db1cb2c6c01fa7e71a314f5e5beb060a/.pre-commit-config.yaml).

In some cases, the right resolution to an open issue might be tangential to the `dbt-core` codebase. The right path forward might be a documentation update or a change that can be made in user-space. In other cases, the issue might describe functionality that the `dbt-core` maintainers are unwilling or unable to incorporate into the `dbt-core` codebase. When it is determined that an open issue describes functionality that will not translate to a code change in the `dbt-core` repository, the issue will be tagged with the `wontfix` label (see below) and closed.

### Using issue labels

The `dbt-core` maintainers use labels to categorize open issues. Most labels describe the domain in the `dbt-core` codebase germane to the discussion.

| tag | description |
| --- | ----------- |
| [triage](https://github.com/dbt-labs/dbt-core/labels/triage) | This is a new issue which has not yet been reviewed by a `dbt-core` maintainer. This label is removed when a maintainer reviews and responds to the issue. |
| [bug](https://github.com/dbt-labs/dbt-core/labels/bug) | This issue represents a defect or regression in `dbt-core` |
| [enhancement](https://github.com/dbt-labs/dbt-core/labels/enhancement) | This issue represents net-new functionality in `dbt-core` |
| [good first issue](https://github.com/dbt-labs/dbt-core/labels/good%20first%20issue) | This issue does not require deep knowledge of the `dbt-core` codebase to implement. This issue is appropriate for a first-time contributor. |
| [help wanted](https://github.com/dbt-labs/dbt-core/labels/help%20wanted) / [discussion](https://github.com/dbt-labs/dbt-core/labels/discussion) | Conversation around this issue in ongoing, and there isn't yet a clear path forward. Input from community members is most welcome. |
| [duplicate](https://github.com/dbt-labs/dbt-core/issues/duplicate) | This issue is functionally identical to another open issue. The `dbt-core` maintainers will close this issue and encourage community members to focus conversation on the other one. |
| [snoozed](https://github.com/dbt-labs/dbt-core/labels/snoozed) | This issue describes a good idea, but one which will probably not be addressed in a six-month time horizon. The `dbt-core` maintainers will revist these issues periodically and re-prioritize them accordingly. |
| [stale](https://github.com/dbt-labs/dbt-core/labels/stale) | This is an old issue which has not recently been updated. Stale issues will periodically be closed by `dbt-core` maintainers, but they can be re-opened if the discussion is restarted. |
| [wontfix](https://github.com/dbt-labs/dbt-core/labels/wontfix) | This issue does not require a code change in the `dbt-core` repository, or the maintainers are unwilling/unable to merge a Pull Request which implements the behavior described in the issue. |

#### Branching Strategy

`dbt-core` has three types of branches:

- **Trunks** are where active development of the next release takes place. There is one trunk named `main` at the time of writing this, and will be the default branch of the repository.
- **Release Branches** track a specific, not yet complete release of `dbt-core`. Each minor version release has a corresponding release branch. For example, the `0.11.x` series of releases has a branch called `0.11.latest`. This allows us to release new patch versions under `0.11` without necessarily needing to pull them into the latest version of `dbt-core`.
- **Feature Branches** track individual features and fixes. On completion they should be merged into the trunk branch or a specific release branch.

## Getting the code

### Installing git

You will need `git` in order to download and modify the `dbt-core` source code. On macOS, the best way to download git is to just install [Xcode](https://developer.apple.com/support/xcode/).

### External contributors

If you are not a member of the `dbt-labs` GitHub organization, you can contribute to `dbt-core` by forking the `dbt-core` repository. For a detailed overview on forking, check out the [GitHub docs on forking](https://help.github.com/en/articles/fork-a-repo). In short, you will need to:

1. fork the `dbt-core` repository
2. clone your fork locally
3. check out a new branch for your proposed changes
4. push changes to your fork
5. open a pull request against `dbt-labs/dbt` from your forked repository

### dbt Labs contributors

If you are a member of the `dbt-labs` GitHub organization, you will have push access to the `dbt-core` repo. Rather than forking `dbt-core` to make your changes, just clone the repository, check out a new branch, and push directly to that branch.

## Setting up an environment

There are some tools that will be helpful to you in developing locally. While this is the list relevant for `dbt-core` development, many of these tools are used commonly across open-source python projects.

### Tools

A short list of tools used in `dbt-core` testing that will be helpful to your understanding:

- [`tox`](https://tox.readthedocs.io/en/latest/) to manage virtualenvs across python versions. We currently target the latest patch releases for Python 3.7, Python 3.8, and Python 3.9
- [`pytest`](https://docs.pytest.org/en/latest/) to discover/run tests
- [`make`](https://users.cs.duke.edu/~ola/courses/programming/Makefiles/Makefiles.html) - but don't worry too much, nobody _really_ understands how make works and our Makefile is super simple
- [`flake8`](https://flake8.pycqa.org/en/latest/) for code linting
- [`black`](https://github.com/psf/black) for code formatting
- [`mypy`](https://mypy.readthedocs.io/en/stable/) for static type checking
- [Github Actions](https://github.com/features/actions)

A deep understanding of these tools in not required to effectively contribute to `dbt-core`, but we recommend checking out the attached documentation if you're interested in learning more about them.

#### virtual environments

We strongly recommend using virtual environments when developing code in `dbt-core`. We recommend creating this virtualenv
in the root of the `dbt-core` repository. To create a new virtualenv, run:
```sh
python3 -m venv env
source env/bin/activate
```

This will create and activate a new Python virtual environment.

#### docker and docker-compose

Docker and docker-compose are both used in testing. Specific instructions for you OS can be found [here](https://docs.docker.com/get-docker/).


#### postgres (optional)

For testing, and later in the examples in this document, you may want to have `psql` available so you can poke around in the database and see what happened. We recommend that you use [homebrew](https://brew.sh/) for that on macOS, and your package manager on Linux. You can install any version of the postgres client that you'd like. On macOS, with homebrew setup, you can run:

```sh
brew install postgresql
```

## Running `dbt-core` in development

### Installation

First make sure that you set up your `virtualenv` as described in [Setting up an environment](#setting-up-an-environment).  Also ensure you have the latest version of pip installed with `pip install --upgrade pip`. Next, install `dbt-core` (and its dependencies) with:

```sh
make dev
# or
pip install -r dev-requirements.txt -r editable-requirements.txt
```

When `dbt-core` is installed this way, any changes you make to the `dbt-core` source code will be reflected immediately in your next `dbt-core` run.


### Running `dbt-core`

With your virtualenv activated, the `dbt-core` script should point back to the source code you've cloned on your machine. You can verify this by running `which dbt`. This command should show you a path to an executable in your virtualenv.

Configure your [profile](https://docs.getdbt.com/docs/configure-your-profile) as necessary to connect to your target databases. It may be a good idea to add a new profile pointing to a local postgres instance, or a specific test sandbox within your data warehouse if appropriate.

## Testing

Getting the `dbt-core` integration tests set up in your local environment will be very helpful as you start to make changes to your local version of `dbt-core`. The section that follows outlines some helpful tips for setting up the test environment.

Although `dbt-core` works with a number of different databases, you won't need to supply credentials for every one of these databases in your test environment. Instead you can test all dbt-core code changes with Python and Postgres.

### Initial setup

We recommend starting with `dbt-core`'s Postgres tests. These tests cover most of the functionality in `dbt-core`, are the fastest to run, and are the easiest to set up. To run the Postgres integration tests, you'll have to do one extra step of setting up the test database:

```sh
make setup-db
```
or, alternatively:
```sh
docker-compose up -d database
PGHOST=localhost PGUSER=root PGPASSWORD=password PGDATABASE=postgres bash test/setup_db.sh
```

### Test commands

There are a few methods for running tests locally.

#### Makefile

There are multiple targets in the Makefile to run common test suites and code
checks, most notably:

```sh
# Runs unit tests with py38 and code checks in parallel.
make test
# Runs postgres integration tests with py38 in "fail fast" mode.
make integration
```
> These make targets assume you have a local install of a recent version of [`tox`](https://tox.readthedocs.io/en/latest/) for unit/integration testing and pre-commit for code quality checks,
> unless you use choose a Docker container to run tests. Run `make help` for more info.

Check out the other targets in the Makefile to see other commonly used test
suites.

#### `pre-commit`
[`pre-commit`](https.pre-commit.com) takes care of running all code-checks for formatting and linting. Run `make dev` to install `pre-commit` in your local environment.  Once this is done you can use any of the linter-based make targets as well as a git pre-commit hook that will ensure proper formatting and linting.

#### `tox`

[`tox`](https://tox.readthedocs.io/en/latest/) takes care of managing virtualenvs and install dependencies in order to run tests. You can also run tests in parallel, for example, you can run unit tests for Python 3.7, Python 3.8, and Python 3.9 checks in parallel with `tox -p`. Also, you can run unit tests for specific python versions with `tox -e py37`. The configuration for these tests in located in `tox.ini`.

#### `pytest`

Finally, you can also run a specific test or group of tests using [`pytest`](https://docs.pytest.org/en/latest/) directly. With a virtualenv
active and dev dependencies installed you can do things like:
```sh
# run specific postgres integration tests
python -m pytest -m profile_postgres test/integration/001_simple_copy_test
# run all unit tests in a file
python -m pytest test/unit/test_graph.py
# run a specific unit test
python -m pytest test/unit/test_graph.py::GraphTest::test__dependency_list
```
> [Here](https://docs.pytest.org/en/reorganize-docs/new-docs/user/commandlineuseful.html)
> is a list of useful command-line options for `pytest` to use while developing.

## Adding CHANGELOG Entry

We use [changie](https://changie.dev) to generate `CHANGELOG` entries.  Do not edit the `CHANGELOG.md` directly.  Your modifications will be lost.

Follow the steps to [install `changie`](https://changie.dev/guide/installation/) for your system.

Once changie is installed and your PR is created, simply run `changie new` and changie will walk you through the process of creating a changelog entry.  Commit the file that's created and your changelog entry is complete!

## Submitting a Pull Request

dbt Labs provides a CI environment to test changes to specific adapters, and periodic maintenance checks of `dbt-core` through Github Actions. For example, if you submit a pull request to the `dbt-redshift` repo, GitHub will trigger automated code checks and tests against Redshift.

A `dbt-core` maintainer will review your PR. They may suggest code revision for style or clarity, or request that you add unit or integration test(s). These are good things! We believe that, with a little bit of help, anyone can contribute high-quality code.
- First time contributors should note code checks + unit tests require a maintainer to approve.


Once all tests are passing and your PR has been approved, a `dbt-core` maintainer will merge your changes into the active development branch. And that's it! Happy developing :tada:

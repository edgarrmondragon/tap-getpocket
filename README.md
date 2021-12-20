# `tap-pocket`

[![Test](https://github.com/edgarrmondragon/tap-pocket/actions/workflows/ci_workflow.yml/badge.svg)](https://github.com/edgarrmondragon/tap-pocket/actions/workflows/ci_workflow.yml)

Pocket tap class.

Built with the [Meltano SDK](https://sdk.meltano.com) for Singer Taps and Targets.

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`

## Settings

| Setting     | Required | Default | Description |
|:------------|:--------:|:-------:|:------------|
| consumer_key| True     | None    | Pocket application key |
| access_token| True     | None    | Pocket user access token |
| start_date  | False    | None    | The earliest record datetime to sync as a UNIX timestamp |

A full list of supported settings and capabilities is available by running: `tap-pocket --about`

## Installation

```bash
pipx install git+https://github.com/edgarrmondragon/tap-pocket.git
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-pocket --about
```

### Source Authentication and Authorization

1. Create a Pocket application: https://getpocket.com/developer/apps/new.
1. Use the app's consumer key to make a request to the `/v3/oauth/request` with ru endpoint to get a `request_token` (`code`).
1. Use the `request_token` to get authorization from the Pocket user: `https://getpocket.com/auth/authorize?request_token=<request_token>&redirect_uri=<redirect_uri>`.
1. Make a request to the `/v3/oauth/authorize` endpoint to get an `access_token`.
1. Put `consumer_key` and `access_token` in a JSON config file.

Documentation: https://getpocket.com/developer/docs/authentication

## Usage

You can easily run `tap-pocket` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-pocket --version
tap-pocket --help
tap-pocket --config CONFIG --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_pocket/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-pocket` CLI interface directly using `poetry run`:

```bash
poetry run tap-pocket --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-pocket
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-pocket --version
# OR run a test `elt` pipeline:
meltano elt tap-pocket target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.

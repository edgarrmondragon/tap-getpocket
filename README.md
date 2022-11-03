# `tap-getpocket`

[![Test](https://github.com/edgarrmondragon/tap-getpocket/actions/workflows/ci_workflow.yml/badge.svg)](https://github.com/edgarrmondragon/tap-getpocket/actions/workflows/ci_workflow.yml)

Pocket tap class.

Built with the [Meltano Singer SDK](https://sdk.meltano.com).

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| consumer_key        | True     | None    | Pocket application key |
| access_token        | True     | None    | Pocket user access token |
| start_date          | False    | None    | The earliest record datetime to sync as a UNIX timestamp |
| favorite            | False    | None    | Set to `true` to sync only favorite items, `false` to sync only non-favorite items, or omit to sync all items |
| content_type        | False    | None    | The content type of items to sync. By default, all content types are synced. |
| state               | True     | all     | Type of item state to sync. By default, all states are synced. |
| tag                 | False    | None    | The tag to sync. By default, all tags are synced. Use `_untagged_` to sync untagged items. |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |

A full list of supported settings and capabilities is available by running: `tap-getpocket --about`

## Installation

```bash
pipx install git+https://github.com/edgarrmondragon/tap-getpocket.git
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-getpocket --about
```

### Source Authentication and Authorization

1. Create a Pocket application: https://getpocket.com/developer/apps/new.
1. Use the app's consumer key to make a request to the `/v3/oauth/request` with ru endpoint to get a `request_token` (`code`).
1. Use the `request_token` to get authorization from the Pocket user: `https://getpocket.com/auth/authorize?request_token=<request_token>&redirect_uri=<redirect_uri>`.
1. Make a request to the `/v3/oauth/authorize` endpoint to get an `access_token`.
1. Put `consumer_key` and `access_token` in a JSON config file.

Documentation: https://getpocket.com/developer/docs/authentication

## Usage

You can easily run `tap-getpocket` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-getpocket --version
tap-getpocket --help
tap-getpocket --config CONFIG --discover > ./catalog.json
```

## Developer Resources

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

You can also test the `tap-getpocket` CLI interface directly using `poetry run`:

```bash
poetry run tap-getpocket --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-getpocket
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-getpocket --version
# OR run a test `elt` pipeline:
meltano elt tap-getpocket target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.

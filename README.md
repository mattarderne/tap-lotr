# tap-lotr

`tap-lotr` is a Singer tap for lotr.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

Data from the free Lord of the Rings [the-one-api.dev](https://the-one-api.dev/documentation) API which requires an account.

Note - uncomment the rest of the streams in `STREAM_TYPES` in `tap_lotr/tap.py` but watch out for rate-limiting and throttling of the API if you do.

## Installation

```bash
pipx install tap-lotr
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-lotr --about
```

### Source Authentication and Authorization

- Create an account at [the-one-api.dev](https://the-one-api.dev/documentation)
- Create a `config.json` file with the below details

```json
{
    "api_key": "<api-key>", 
    "api_url": "https://the-one-api.dev/v2"
}
```

## Usage

You can easily run `tap-lotr` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-lotr --version
tap-lotr --help
tap-lotr --config config.json --discover > ./catalog.json
```

Run with poetry
```bash
poetry run tap-lotr --config config.json
```

## Developer Resources

- Use the `.vscode/launch.json` for debugging if you use VSCode. 

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_lotr/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-lotr` CLI interface directly using `poetry run`:

```bash
poetry run tap-lotr --help
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
cd tap-lotr
meltano install
```


Set variables and API token
```bash
meltano config tap-lotr set api_url https://the-one-api.dev/v2
meltano config tap-lotr set api_key <your_api_key>
```

Install a test loader
```bash
meltano add loader target-jsonl
```

Now you can test and orchestrate using Meltano:

Run meltano
```bash
# Test invocation:
meltano invoke tap-lotr --version
# OR run a test `elt` pipeline:
meltano elt tap-lotr target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.

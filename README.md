# Short URLs Client
![CI](https://github.com/jamesridgway/short-urls-client/workflows/CI/badge.svg?branch=master)

A python client for my [aws-lambda-short-url](https://github.com/jamesridgway/aws-lambda-short-url) project.

## Installation

    pip install short-urls-client

## Usage

### Setup credentials

    short-urls config -d mydoma.in -a MyApiKey-l3tm31n

### List all URLs

    short-urls list

### Create a URL

    short-urls create https://github.com/jamesridgway/short-urls-client

Or specify a custom token (e.g. `python-client`)

    short-urls create https://github.com/jamesridgway/short-urls-client python-client

### Delete a URL

    short-urls delete https://mydoma.in/T0k3N

## Development
The following instructions will help you get started in developing changes for this project.

### Python Environment
Run the following to setup a python virtual environment and install all dependencies:

    ./setup.sh

### Pylint
Pylint is used to check code quality and style, pylint can be run using:

    ./run-pylint.sh

### Tests
You can run the test as follows:

    ./run-tests.sh

An HTML code coverage report will be generated in the `htmlcov` directory.

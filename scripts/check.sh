#!/bin/sh -e

export SOURCE_FILES="correios tests"

set -x

black --check --diff $SOURCE_FILES
flake8 $SOURCE_FILES
mypy --show-error-codes $SOURCE_FILES
isort --check --diff $SOURCE_FILES
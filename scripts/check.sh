#!/bin/sh -e

export SOURCE_FILES="correios tests"

set -x

black --check --diff --target-version=py36 $SOURCE_FILES
flake8 $SOURCE_FILES
mypy --show-error-codes $SOURCE_FILES
isort --check --diff --project=correios $SOURCE_FILES
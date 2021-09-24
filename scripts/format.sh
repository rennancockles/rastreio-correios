#!/bin/sh -e

export SOURCE_FILES="correios tests"

set -x

black $SOURCE_FILES
isort $SOURCE_FILES
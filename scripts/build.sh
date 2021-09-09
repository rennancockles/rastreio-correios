#!/bin/sh -e

set -x

python setup.py sdist bdist_wheel
twine check dist/*
mkdocs build
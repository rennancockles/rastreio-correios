#!/bin/sh -e

REQUIREMENTS="requirements.txt"

[[ $@ =~ -[dD] ]] && REQUIREMENTS="dev-requirements.txt"

set -x

pip install -r "$REQUIREMENTS"

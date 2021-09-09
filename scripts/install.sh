#!/bin/sh -e

REQUIREMENTS="requirements.txt"

[ $1 == "-d" -o $1 == "-D" ] && REQUIREMENTS="dev-requirements.txt"

set -x

pip install -r "$REQUIREMENTS"

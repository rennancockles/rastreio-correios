#!/bin/sh -e

set -x

pytest
codecov

#!/bin/sh -e

VERSION_FILE="correios/__init__.py"

if [ ! -z "$GITHUB_ACTIONS" ]; then
  git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
  git config --local user.name "GitHub Action"

  VERSION=`grep __version__ ${VERSION_FILE} | grep -o '[0-9][^"]*'`

  if [ "refs/tags/v${VERSION}" != "${GITHUB_REF}" ] ; then
    echo "GitHub Ref '${GITHUB_REF}' did not match package version '${VERSION}'"
    exit 1
  fi
fi

set -x

twine upload dist/*
mkdocs gh-deploy --force
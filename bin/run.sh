#!/bin/sh
# Stimer runner.
set -e

name=stimer

cd ${name}/
poetry run python src/${name} $@

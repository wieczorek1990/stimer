#!/bin/sh
# Runner.
set -e

name=stimer

cd ${name}/
poetry run python src/${name} $@

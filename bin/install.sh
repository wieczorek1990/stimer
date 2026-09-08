#!/bin/sh
# Install script.
set -e

name=stimer

cd ${name}
pip uninstall ${name} -y && pip install --user .

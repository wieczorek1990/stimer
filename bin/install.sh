#!/bin/sh
# Install script.
set -e

name=stimer

cd ${name}
pip3 uninstall ${name} -y && pip3 install --user .

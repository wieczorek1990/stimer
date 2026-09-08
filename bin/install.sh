#!/bin/sh
# Install script.

name=stimer

cd ${name}
pip uninstall ${name} -y && pip install --user .

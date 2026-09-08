#!/bin/sh
# Install script.

name=stimer

pip uninstall {} -y && pip install --user .

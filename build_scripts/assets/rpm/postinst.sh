#!/usr/bin/env bash
# Post install script for the UI .rpm to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/gold/resources/app.asar.unpacked/daemon/gold /usr/bin/gold || true
ln -s /opt/gold/gold-blockchain /usr/bin/gold-blockchain || true

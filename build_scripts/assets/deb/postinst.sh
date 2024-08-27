#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

chown -f root:root /opt/gold/chrome-sandbox || true
chmod -f 4755 /opt/gold/chrome-sandbox || true
ln -s /opt/gold/resources/app.asar.unpacked/daemon/gold /usr/bin/gold || true
ln -s /opt/gold/gold-blockchain /usr/bin/gold-blockchain || true

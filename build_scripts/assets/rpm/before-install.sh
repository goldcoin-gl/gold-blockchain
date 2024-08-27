#!/usr/bin/env bash

set -e

# handling multiple cases where empty directories are left behind resulting
# in issues with the python identifying the blockchain version
find /opt/gold -type d -empty -delete || true

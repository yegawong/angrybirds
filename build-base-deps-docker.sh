#!/bin/bash
set -x

# Build the current Angrybirds source
docker build --no-cache -t angrybirds/base-deps docker/base-deps

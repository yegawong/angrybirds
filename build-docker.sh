#!/bin/bash
set -x

# Build the current Angrybirds source
git rev-parse HEAD > ./docker/deploy/git-rev
git archive -o ./docker/deploy/angrybirds.tar "$(git rev-parse HEAD)"
docker build --no-cache -t angrybirds/deploy docker/deploy
rm ./docker/deploy/angrybirds.tar ./docker/deploy/git-rev

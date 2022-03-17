#!/bin/bash

DIRS="$(find . -type d -not -path ./.actions | tail -n +2 | sed -e "s/\.\///g")"

for DIR in $DIRS
do
    echo "#############################################"
    echo "Building flow $DIR"
    docker build -f Dockerfile --build-arg checklist=$DIR --build-arg registry=ghcr.io/watcherwhale -t ghcr.io/watcherwhale/checklist:$DIR-latest .
done

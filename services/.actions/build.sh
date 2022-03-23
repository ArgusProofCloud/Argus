#!/bin/bash

docker build --no-cache -f Dockerfile --build-arg service=gateway -t ghcr.io/watcherwhale/gateway .
docker build --no-cache -f Dockerfile --build-arg service=sequencer -t ghcr.io/watcherwhale/sequencer .
docker build --no-cache -f Dockerfile.cert --build-arg service=cert-master -t ghcr.io/watcherwhale/cert-master .

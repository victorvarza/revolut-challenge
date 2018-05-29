#!/usr/bin/env bash

# Consider to be part of pipeline (GitLab/Jenkins)
VER=1.0
docker build -t local/revolut:${VER} .

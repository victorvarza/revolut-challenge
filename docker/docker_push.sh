#!/usr/bin/env bash

# Consider to be part of pipeline (GitLab/Jenkins)

if [ $# -lt 1 ]; then
    echo "Usage: $0 DOCKER_HUB_USER"
    exit 1;
fi

DOCKER_HUB_USER=$1
VER=1.0

docker tag local/revolut:${VER} ${DOCKER_HUB_USER}/revolut:${VER}
docker push ${DOCKER_HUB_USER}/revolut:${VER}
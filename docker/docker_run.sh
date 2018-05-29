#!/bin/bash

# for local testing purpose

docker run -d -p 6379:6379 --name redis redis:latest
docker run -d -p 8080:8080 --link redis:redis --name revolut trainersontheweb/revolut:1.0
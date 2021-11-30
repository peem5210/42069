#!/bin/sh
docker-compose -f ./.github/scripts/docker-compose-ci.yml pull
docker-compose -f ./.github/scripts/docker-compose-ci.yml down
#docker network create 42069-backend-net --subnet 172.24.24.0/24
docker-compose -f ./.github/scripts/docker-compose-ci.yml up --build

#!/bin/sh
docker-compose -f ./.github/scripts/docker-compose-ci.yml pull
docker-compose -f ./.github/scripts/docker-compose-ci.yml down
docker-compose -f ./.github/scripts/docker-compose-ci.yml up --build -d

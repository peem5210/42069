#!/bin/sh
docker-compose pull
docker-compose down
docker-compose up --build -d

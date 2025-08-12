#!/bin/bash

docker build -t suid2 -f ./Dockerfile .
docker run --pull=never --network none --memory 128m --cpus 0.5 --pids-limit 50 --ulimit nofile=64:64 --rm -it suid2

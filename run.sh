#!/bin/bash

CONTAINER=gmw-container
 
RUNNING=$(docker inspect --format="{{ .State.Running }}" $CONTAINER 2> /dev/null)

if [ $? -eq 1 ]; then
  echo "'$CONTAINER' does not exist. Creating a new one."
else
  echo "Stopping existing container."
  docker container stop gmw-container
fi

echo "Copy this link to your browser:"
docker run --rm -p 8888:8888 -v $(pwd)/workspace:/usr/src/app/workspace --name gmw-container  gmw:latest
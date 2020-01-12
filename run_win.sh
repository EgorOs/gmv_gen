#!/bin/bash

CONTAINER=gmv-container
 
RUNNING=$(docker inspect --format="{{ .State.Running }}" $CONTAINER 2> /dev/null)

echo ""
echo "------------------------"
echo "ИНСТРУКЦИЯ:"
echo "В адресную строку браузера введите: $(docker-machine ip):8888"
echo "Затем вас попросят ввести Token"
echo "Токен, который следует ввести появится ниже и будет выглядеть примерно как ?token=4ab90d60f52f7e34afaccf083351e37645338ddd9a3b7f25"
echo "В таком случае необходимо скопировать часть без слова token"
echo "К примеру: 4ab90d60f52f7e34afaccf083351e37645338ddd9a3b7f25"
echo "------------------------"
echo ""

if [ $? -eq 1 ]; then
  echo "'$CONTAINER' does not exist. Creating a new one."
else
  echo "Stopping existing container."
  docker container stop gmv-container
fi

export LOCAL_PATH="//$(pwd)/workspace"

echo "Copy this link to your browser:"
docker run --rm -p 8888:8888 -v $LOCAL_PATH:/usr/src/app/workspace --name gmv-container  gmv:latest
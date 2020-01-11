#!/bin/bash

CONTAINER=gmw-container
 
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
  docker run -p 8888:8888 --name gmw-container gmw:latest
else
  echo "Restarting existing container."
  docker container stop gmw-container
  docker container start --attach gmw-container
fi
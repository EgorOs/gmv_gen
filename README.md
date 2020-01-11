# Сборка контейнера

```docker build  --tag gmw .```

# Запуск для UNIX-подобных систем

```docker run --rm -p 8888:8888 -v $(pwd)/workspace:/usr/src/app/workspace --name gmw-container  gmw:latest```
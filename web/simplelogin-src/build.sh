#!/bin/bash
app="simple-login"
docker build -t ${app} .
docker run -d -p 1337:80 \
  --name=${app} \
  -v $PWD:/app ${app}

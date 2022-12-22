# !/bin/bash

docker ps -aq | xargs docker rm -f

cd ..
docker image build -t flaskimg:latest -f Docker/Dockerfile .
docker run -d --publish 5000:5000 --name flaskapp flaskimg:latest

docker logs -f flaskapp

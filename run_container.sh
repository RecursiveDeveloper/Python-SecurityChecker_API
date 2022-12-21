# !/bin/bash

docker ps -aq | xargs docker rm -f
docker image build -t flaskimg:latest .

docker run -d --publish 5000:5000 --name flaskapp flaskimg:latest
docker logs -f flaskapp


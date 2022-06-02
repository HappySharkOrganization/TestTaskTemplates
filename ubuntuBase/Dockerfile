FROM ubuntu:latest

COPY packages.txt .

RUN apt-get update && apt-get install -y < packages.txt



ADD . /runtime/task
WORKDIR /runtime/task/src

ENTRYPOINT ["bash", "main.sh"]

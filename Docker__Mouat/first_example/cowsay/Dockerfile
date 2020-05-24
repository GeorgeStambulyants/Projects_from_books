FROM debian:buster

MAINTAINER George Stambulyants <george.stamb28@gmail.com>

RUN apt-get update && apt-get install -y cowsay fortune
COPY entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]
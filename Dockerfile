FROM python:3.6

MAINTAINER chck

RUN \
  apt-get update

RUN \
  mkdir /work

WORKDIR \
  /work

ADD \
  requirements.txt /work

RUN \
  pip install --upgrade -r requirements.txt


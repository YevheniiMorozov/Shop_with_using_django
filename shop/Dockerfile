FROM python:3.9


RUN apt-get update &&\
    apt-get install -y --no-install-recommends build-essential locales-all

ADD requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /srv

ADD shop/ /srv


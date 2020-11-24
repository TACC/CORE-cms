FROM python:3.6-buster as python-base

LABEL maintainer="TACC-ACI-WMA <wma_prtl@tacc.utexas.edu>"

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y build-essential python3-dev \
    libldap2-dev libsasl2-dev ldap-utils tox \
    lcov valgrind vim && pip3 install uwsgi

RUN mkdir /code

COPY . /code

WORKDIR /code

RUN pip3 install --no-cache-dir -r requirements.txt

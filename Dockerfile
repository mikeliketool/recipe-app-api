FROM python:3.7-alpine
MAINTAINER mikeliketool

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
Run pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements*.txt .

RUN apt-get update && \
    apt-get -y install libpq-dev gcc && \
    pip install --upgrade pip && \
    pip install -r requirements-dev.txt
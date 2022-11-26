FROM python:3.11-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv requirements --dev > requirements.txt && \
    pip install -r requirements.txt

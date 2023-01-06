FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/

RUN apt update -y && apt install -y build-essential libpq-dev

RUN pip3 install poetry

RUN poetry install --no-root

RUN poetry add psycopg2

COPY . /usr/src/app
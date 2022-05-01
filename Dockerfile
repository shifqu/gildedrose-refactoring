# syntax=docker/dockerfile:1

FROM python:3.10-bullseye

WORKDIR /app


# set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DEFAULT_TIMEOUT=30
ENV POETRY_HOME=/poetry
ENV POETRY_VERSION=1.1.13
ENV PATH="$POETRY_HOME/bin:$PATH"

# install system dependencies
RUN apt-get update \
  && apt-get -y install curl git shellcheck \
  && apt-get clean

# install and configure poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# copy and install python requirements to cache them (lock-file might not exist initially, so wildcard it)
COPY ./poetry.loc[k] ./pyproject.toml ./
RUN poetry install --no-dev

# copy all files belonging to the project.
COPY . .
RUN poetry install

CMD ["python"]

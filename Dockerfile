FROM python:3.11.0

WORKDIR /ig_posts_patser_test_task

ENV POETRY_VERSION=1.2.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry update
RUN apt-get update
RUN apt-get install dos2unix

COPY .env .env

COPY . .

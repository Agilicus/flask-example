FROM python:3.10.6-slim-buster as build

RUN : \
 && pip install poetry

EXPOSE 5001

COPY . /app
WORKDIR /app

RUN : \
 && poetry config virtualenvs.create false \
 && poetry install --no-dev \
 && adduser --disabled-password --gecos '' web

# USER web

ENTRYPOINT ["poetry", "run", "python", "-m", "api.main" ]



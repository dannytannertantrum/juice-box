FROM python:3.7-slim

WORKDIR /opt/api

RUN \
  apt-get update \
  && apt-get install -y gcc libpq-dev bash \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./requirements.txt
COPY ./pytest.ini ./pytest.ini

RUN pip install -r requirements.txt

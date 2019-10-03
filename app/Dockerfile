FROM python:3.7-slim

WORKDIR /app

RUN \
  apt-get update \
  && apt-get install -y gcc libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt

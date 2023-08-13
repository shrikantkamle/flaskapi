FROM python:3-alpine3.18

WORKDIR /app
COPY . /app
COPY requirement.txt .

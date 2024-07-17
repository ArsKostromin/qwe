FROM python:3.11.9-alpine3.20

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    postgresql-dev \
    build-base \
    python3-dev \
    jpeg-dev \
    zlib-dev

COPY requirements.txt /temp/requirements.txt 
COPY service /service
WORKDIR /service
EXPOSE 8000

RUN pip install --upgrade pip

RUN pip install -r /temp/requirements.txt 

RUN adduser --disabled-password service-user

USER service-user
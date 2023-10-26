# This is a multi-stage Dockerfile

# syntax=docker/dockerfile:1.6.0
# Image used for build. Assigned the name for the image.
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

# working directory inside the container
WORKDIR /app

# copies the .txt from host to /app inside the container
COPY requirements.txt /app
# install python dependencies listed in requirements.txt, using cache for build speed
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app


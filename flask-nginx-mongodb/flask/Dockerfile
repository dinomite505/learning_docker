# syntax=docker/dockerfile:experimental
# Defining the platform stage, image and start of builder stage
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

# Setting to /src where app's source code will be copied
WORKDIR /src
# Copies req. from host to /src in the container
COPY requirements.txt /src
# Installs Python packages listed in requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install requirements.txt
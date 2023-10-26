# This is a multi-stage build Dockerfile

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

# copying contents of the Flask app directory from host to container at /app
COPY . /app

# setting entrypoint to execute Python3 and defautl command is to run 'app.py'
ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM baseImage

RUN <<EOF
apk update
apk add git
EOF

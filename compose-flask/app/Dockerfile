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

# create new build stage based on build stage 'builder'
FROM builder as dev-envs

# run commands to install dependencies. Enclosed within the script block
# you can also use ampersand (&&) to separate multiple shell commands
RUN <<EOF
apk update
apk add git
EOF

# Add user and group to Docker image
# created a new group with 'addgroups' to manage user access
# created new user "dino" within the Docker image and placed the user to "docker" group
# user's default shell defined as /bin/bash
RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker dino
EOF

# install Docker tools/plugins (cli, buildx, scan, compose) from DockerHub image
COPY --from=gloursdocker/docker / /

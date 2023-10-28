# syntax=docker/dockerfile:experimental

# 1ST BUILD STAGE
# Defining the platform stage, image and start of builder stage
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

# Setting to /src where app's source code will be copied
WORKDIR /src
# Copies req. from host to /src in the container

COPY requirements.txt /src
# Installs Python packages listed in requirements.txt
# Build cache for pip should speed up the install
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .

# When container is started it runs Python script server.py
CMD [ "python3", "server.py" ]

# 2ND BUILD STAGE
# Beginning with `dev-envs' stage, based on builder stage
FROM builder as dev-envs

# Updates Alpine package manager and installs git
RUN <<EOF
apk update
apk add git
EOF

# Creates a group and creates user 'dino' and assigns it to that group
# (-S system group) = lower GID and no password in /etc/group
RUN <<EOF
addgroup -S docker 
adduser -S --shell /bin/bash --ingroup docker dino
EOF

# Copies from external image to install Docker tools
COPY --from=gloursdocker/docker / /

# Runs server.py script once container is started
CMD [ "python3", "server.py" ]

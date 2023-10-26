# Building Dockerfile from scratch

# NOTE: You'll find how to run this with other info in README.md

# Using official 'node' image with Alpine branch
FROM node:alpine:3.18.4

# This app will listen on port 3000
EXPOSE 3000

# Thid image will use alpine package manager to install 'tini'
RUN apk --update tini

# Create a directory for app files
RUN mkdir -p /usr/src/app

# Node uses a "package manager" so it needs to copy in package.json
WORKDIR /usr/src/app

# 

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

# Installs 'npm' and temporary cache (ampersand to install one after the other)
RUN npm install && npm install --cache /tmp/empty-cache
# As of npm@5. the npm cache self-heals from corruption issues so 'npm cache clean' isn't necessary
# Data extratced from the cache is guaranteed to be valid.
# If you want to make sure everything is consistent use 'npm cache verify'.
# I'm using if I'm potentially debugging an issue with the installer 
# Deleting the cache can only make npm go slower.

# Copy in all files from current directory on the host to the current direcotry in the image 
COPY . .

# It starts the container using 'tini
CMD ["tini", "node", "./bin/www"]
# this is exec form that is prefered by Docker and it is in JSON format.
# when the container is started from an image it will execute 'tini' as PID1 initial process, which
# then starts the Node.js process with ./bin/www script (check bin folder)
## Build Node.js image with Dockerfile

The primary goal of this project is to package and distribute a Node.js application within a Docker container. This application is already fully developed, tested, and pre-built, meaning it contains all the necessary dependencies and configurations to run without any issues.

### Dockerfile

These are the layers we are building the image on. You can find detailed explanation for each command in the actual Dockerfile.

[_Dockerfile_](Dockerfile)
```
FROM node:alpine:3.18.4
EXPOSE 3000
RUN apk --update tini
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN npm install && npm install --cache /tmp/empty-cache
COPY . .
CMD ["tini", "node", "./bin/www"]
```

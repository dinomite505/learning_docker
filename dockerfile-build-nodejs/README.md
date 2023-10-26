# Build an Image from a Dockerfile

The primary goal of this project is to package and distribute a Node.js application within a Docker container. This application is already fully developed, tested, and pre-built, meaning it contains all the necessary dependencies and configurations to run without any issues.

Pre-pulling **node** and **alpine** images and having them locally can increase efficiency and avoid any potential delays during the Docker image build process. Do so with:

```
docker pull node
docker pull alpine:3.18.4
```


## Dockerfile

These are the layers we are building the image on. You can find detailed explanation for each command in the [_Dockerfile_](Dockerfile)

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


## Build the image

Make sure you have a valid Dockerfile in the current directory, and the Docker daemon is running for this command to work as expected.
```
docker build -t testnode .
```
If you decide to make changes to your app (HTML, styles..) you won't see changes until you rebuild the app.


## Run the image in the container

```
docker container run --rm -p 80:3000 testnode
´´´
Container is not detached so you can see HTTP access logs entries and it is removed once you exit.








You will see GET requests similar to this:
```
GET / 200 38.482 ms - 290
GET /stylesheets/style.css 200 4.367 ms - 111
GET /images/picard.gif 200 2.493 ms - 417700
GET /favicon.ico 404 6.763 ms - 970
```


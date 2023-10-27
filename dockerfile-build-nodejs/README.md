# Build an Image from a Dockerfile

The primary goal of this project is to package and distribute a Node.js application within a Docker container. This application is already fully developed, tested, and pre-built, meaning it contains all the necessary dependencies and configurations to run without any issues.

Pre-pulling **node** and **alpine** images and having them locally can increase efficiency and avoid any potential delays during the Docker image build process. NOTE: You can use any version(tag) of these images. Just make sure you specify that in your Dockerfile.

```
docker pull node
docker pull alpine:3.17
```
## Project Structure

```
.
├── Dockerfile
├── README.md
├── app.js
├── bin
│     └── www    
├── node_modules
│   └── ...
├── package.json
├── public
│    ├── images
│    └── stylesheets
├── routes
│   ├── index.js
│   └── users.js
├── views
    ├── error.hbs
    ├── index.hbs
    └── layout.hbs
```
<br>

## Dockerfile

These are the layers we are building the image on. You can find detailed explanation for each command in your [_Dockerfile_](Dockerfile)

```
FROM node:21-alpine3.17
EXPOSE 3000
RUN apk add --update tini
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json package.json
RUN npm install && npm cache verify
COPY . .
CMD ["tini", "node", "./bin/www"]
```
<br>

## Build the image

Make sure you have a valid Dockerfile in the current directory, and the Docker daemon is running for this command to work as expected. Usage: `docker build [OPTIONS] PATH | URL | -`
```
docker build -t testnode .
```

### Expected Output:
```
[+] Building 5.7s (12/12) FINISHED                                             docker:default
 => [internal] load build definition from Dockerfile                                     0.0s
 => => transferring dockerfile: 1.43kB                                                   0.0s
 => [internal] load .dockerignore                                                        0.0s
 => => transferring context: 448B                                                        0.0s
 => [internal] load metadata for docker.io/library/node:21-alpine3.17                    0.6s
 => [1/7] FROM docker.io/library/node:21-alpine3.17@sha256:c8e4f0ad53631bbf60449e394a33  0.0s
 => [internal] load build context                                                        0.0s
 => => transferring context: 682B                                                        0.0s
 => CACHED [2/7] RUN apk update tini                                                     0.0s
 => CACHED [3/7] RUN mkdir -p /usr/src/app                                               0.0s
 => CACHED [4/7] WORKDIR /usr/src/app                                                    0.0s
 => [5/7] COPY package.json package.json                                                 0.0s
 => [6/7] RUN npm install && npm cache verify                                            4.8s
 => [7/7] COPY . .                                                                       0.0s
 => exporting to image                                                                   0.2s
 => => exporting layers                                                                  0.1s
 => => writing image sha256:8e2094700e47a07e7c37607a2eef90d758f60e0db099482a926e56401d1  0.0s
 => => naming to docker.io/library/testnode                                              0.0s
```
```
docker image ls
```

#### Note
If you decide to make changes to your application code, they won't be automatically reflected in a running Docker container until you **rebuild the image** and recreate the container.

<br>

## Run the image in the container
```
docker container run --rm -p 80:3000 testnode
```

Container is not detached so you can see HTTP access logs entries and it is removed once you exit.

Open your browser and navigate to `localhost` to see the app.

Is Captain Picard applauding you? Great!

<br>

Back in the container, you will see a stream of GET requests similar to this:
```
GET / 200 38.482 ms - 290
GET /stylesheets/style.css 200 4.367 ms - 111
GET /images/picard.gif 200 2.493 ms - 417700
GET /favicon.ico 404 6.763 ms - 970
```
<br>

## Output Screenshot
![nodeapp](https://github.com/dinomite505/learning_docker/assets/131146683/8952bb9b-565a-4912-a00a-a7aca212e33f)

## Testing

Run additional test by pushing, pulling to Docker Hub or by removing your image locally and running it again to see how it behaves.

<br>

If you list your images with `docker image ls` you will see your `testnode` image tagged as `latest`. <br>
You can name your image with `docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]` so follow `repository:tag` format:

```
docker tag testnode repository_name/testing-node
```
<br>

##### Note
Make sure you are logged in with `docker login` **before** pushing.

<br>

Usage: `docker push [OPTIONS] NAME[:TAG]` so in our case we're going to push this image without using `OPTIONS`:

```
docker push repository_name/testing-node
```
Confirm the push on your Docker Hub account, and from terminal use `docker image ls` to verify.

<br>

Remove the image locally `docker image rm repository_name/testing-node`. 

Then, to download and run it again use `docker container run --rm -p 80:3000 repository_name/testing-node`.

Open `localhost` and refresh. Check terminal streams to confirm.

<br>

#### Note 
**Clean everything up once you're done.**
```
docker ps -a
```
```
docker container prune
```

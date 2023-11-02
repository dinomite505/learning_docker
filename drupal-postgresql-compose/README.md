# Building a Compose File for Drupal and PostgreSQL Project
<br>

## Assignment Info

What you need to do in this project:
<br>

* Build a basic compose file for a Drupal content management system website.
* Using drupal:9 image along with postgres:14 image (Drupal needs database running behind it)
* Use DockerHub documentation on these images to get more information
* Use ports inside of the compose file to expose Drupal on 8080 so you can localhost:8080
* Be sure to set POSTGRES_PASSWORD for postgres service
* Walk through Drupal setup via browser once you start with `docker compose up`
* Tip: Drupal assumes DB is **localhost**, but it is service name
* Extra Credit: Use volumes to store Drupal unique data

- - - -
<br>

## Solution

1. Create a `docker compose.yaml` file, define services, and volumes. Use DockerHub!
```

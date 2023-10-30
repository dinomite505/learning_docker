# Run and Test Containers

In this assignment we will be running multiple different containers, create a custom network and connect those containers to it, test their connection and clean everything up. We will be using Nginx, Apache and MySQL images for our containers. This practice will give you insight to essential Docker commands and how containers work in general.

<br>

## Assignment info
<br>

1. Run three containers (Nginx, Apache and MySQL) using corresponding Docker images (MySQL needs to have environment variable set)
2. Containers should run in the background (detached)
3. Name the containers
4. Assign the appropriate ports to each of them
5. Create a custom network and assign each containers to it (this can be done upon container creation or as a separate task)
6. Check if all containers are created
7. Inspect your custom network to see if all containers are assigned to it
8. Test the ports of all three containers
9. Stop and remove containers, confirm it and remove the images if needed

<br>

## Running containers

#### **Nginx**
```
docker container run -d --name proxy -p 80:80 nginx
```

#### **Apache (HTTPD)**
```
docker container run -d --name webserver -p 8080:80 httpd
```

#### **MySQL**
```
docker container run -d --name db -p 3306:3306 -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql
```
<br>
<br>


*Explanation*
<br>

`docker container run` create and starts a new Docker container from a specified image.
<br>

`-d (or --detach)` option(flag) runs container in detached mode and it is **running in the background** which means you can continue using your terminal without being tied to the container's output. Upon creatin in detached mode you will get a unique container ID. If you don't specify `-d` your container **will run in the foreground** and you will see container's STDOUT and STDERR streams. To exit the container running in foreground use `CTRL+C`.
<br>

`--name <name>` assigns a name to the container. If you don't specify a containers name upon creation, one will be assigned to it automatically by Docker.
<br>

`-p <port>` part exposes our local port 80 on our host( local machine) and sends all traffic from it to executable running inside that container on port 80 (routes the traffic to the container IP on port 80). DOcker publishing format is `<public_port:container_port>`. 
<br>

`-e (or --env) MYSQL_RANDOM_ROOT_PASSWORD=yes mysql` when you are running MySQL container it is a good practice to set the environment variable to instruct MySQL to generate a root password during its initialization. 
In this case we are generating a random password which you can find using `docker container logs <name>`.
<br>

When you open logs, locate `GENERATED ROOT PASSWORD` section to see your MySQL password.
<br>

You can also use `-e MYSQL_ALLOW_EMPTY_PASSWORD=yes` allowing to start MySQL container with an empty root password (not recommended for production environments) or `-e MYSQL_ROOT_PASSWORD=my_secret_password` to set a specific password of your choice.
<br>

## Docker Networks









docker container top
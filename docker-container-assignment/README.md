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

## Creating and Starting Containers

### **Nginx**
```
docker container run -d --name proxy -p 80:80 nginx
```

### **Apache (HTTPD)**
```
docker container run -d --name webserver -p 8080:80 httpd
```

### **MySQL**
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

`-p <port>` part exposes our local e.g. port 80 on our host( local machine) and sends all traffic from it to executable running inside that container on port 80 (routes the traffic to the container IP on port 80) allowing external communication with services running inside the container. Docker publishing format is `<public_port:container_port>`. 
<br>

`-e (or --env) MYSQL_RANDOM_ROOT_PASSWORD=yes mysql` when you are running MySQL container it is a good practice to set the environment variable to instruct MySQL to generate a root password during its initialization. 
In this case we are generating a random password which you can find using `docker container logs <name>`.
<br>

When you open logs, locate `GENERATED ROOT PASSWORD` section to see your MySQL password.
<br>

You can also use `-e MYSQL_ALLOW_EMPTY_PASSWORD=yes` allowing to start MySQL container with an empty root password (not recommended for production environments) or `-e MYSQL_ROOT_PASSWORD=my_secret_password` to set a specific password of your choice.
<br>
<br>

## Docker Networks

### --network bridge
When we start a new container, and don't specify the network, it will automatically use the default virtual `bridge` network. Each container within bridge network gets its own IP address and they use Network Address Translation (NAT) configuration that maps container IP addresses to the host machine's IP address. Bridge network brings **isolation** from the host and other containers and container's **inter-communication**.
<br>

### --network host
Host network gains performance by skipping virtual networks and attaches the container **directly to the host interface**, rather than creating a separate network for the container. This means that the container shares the same network stack as the host machine making the container's network interface and ports directly accessible on the host's network. This **sacrifices security** of container model (prevents the security boundaries of the containerization from protecting the interface of that container).
<br>

### --network none
This option is used to completely disable networking for a container. If connected to it, the container has no network connectivity, it cannot communicate with the host, other containers or external networks. This is useful for scenarios where network access is not required and in security-sensitive cases where network must be restricted.
<br>
<br>

**To list** your networks:
```
docker network ls
```
#### Output
```
NETWORK ID     NAME      DRIVER    SCOPE
623f161289a7   bridge    bridge    local
8ff3c28c9add   host      host      local
2b25473ca5bc   none      null      local
```
<br>

Upon the creation of our containers we could've create a new container, and new network, and assign this container to it in one command like this:
<br>

```
docker container run -d --name proxy -p 80:80 --network my_app_net
```
We will focus on creating our own custom network for our three containers:
<br>

```
docker network create my_app_net
```
This command will create our new custom network and if you list your networks with `docker network ls` you will see it uses a *bridge driver*. `Network drivers` are built-in or 3rd-party extensions that give you virtual network features.
<br>
<br>

## Connecting and Disconnecting Containers to/from Custom Networks
Next, we will use `docker container ls` to list our containers.
<br>

```
$ docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                                  NAMES
c88b044717d1   nginx     "/docker-entrypoint.…"   28 seconds ago       Up 27 seconds       0.0.0.0:80->80/tcp, :::80->80/tcp                      proxy
edab2d7a9814   httpd     "httpd-foreground"       45 seconds ago       Up 44 seconds       0.0.0.0:8080->80/tcp, :::8080->80/tcp                  webserver
abdbbdeea6c6   mysql     "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   db
```

<br>

When you want to connect your container to the specific network you can use either their name or ID's. **Note:** You can type in first couple of characters from container's ID, just so it's unique.
**USAGE:**`docker network connect <network_name_or_ID> <container_name_or_ID>`
```
docker network connect my_app_net proxy
```
```
docker network connect my_app_net webserver
```
```
docker network connect my_app_net db
```








docker container top
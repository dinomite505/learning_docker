# Run and Test Containers

In this assignment we will be running multiple different containers, create a custom network and connect those containers to it, test their connection, and clean everything up. We will be using Nginx, Apache and MySQL images for our containers. This short project will give you insight to essential Docker commands and how containers work in general.

<br>

## Assignment info :clipboard:
<br>

* Run three containers (Nginx, Apache and MySQL) keeping the following in mind:
    * Containers should run in the background (detached)
    * Name the containers
    * Assign the ports correctly to each of them
    * Check if all containers are created
    * MySQL needs to have environment variable set
* Create a custom network 
    * Connect that each container is connected to it
* Inspect your custom network to see if all containers are assigned to it
* Test the ports of all three containers (from terminal and in browser)
* Clean Up!
    * Stop and remove containers
    * Confirm that containers are removed
    * Remove the images and network if needed


- - - -

## Creating and Starting Containers :gear:

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

:bulb: Before you run these containers, let's see what all these commands, options and arguments actually do:

<br>

`docker container run` create and starts a new Docker container from a specified image.
<br>

`-d (or --detach)` option(flag) runs container in detached mode and it is **running in the background** which means you can continue using your terminal without being tied to the container's output. Upon creating in detached mode you will get a unique container ID. If you don't specify `-d` your container **will run in the foreground** and you will see container's `STDOUT` and `STDERR` streams. To exit the container running in foreground use `CTRL+C`.
<br>

`--name <name>` assigns a name to the container. If you don't specify a containers name upon creation, one will be assigned to it automatically by Docker.
<br>

`-p <port>` part exposes our local e.g. port 80 on our host( local machine) and sends all traffic from it to executable running inside that container on port 80 (routes the traffic to the container IP on port 80) allowing external communication with services running inside the container. Docker publishing format is `<public_port:container_port>`. Problem occur when multiple services are running on the same public host port, not in multiple containers, because each container gets its own internal IP behind NAT, so the ports won't conflict across two container network interfaces.❗NUMBER ON THE LEFT MUST BE DIFFERENT❗.

<br>

`-e (or --env) MYSQL_RANDOM_ROOT_PASSWORD=yes mysql` when you are running MySQL container, it is a good practice to set the environment variable to instruct MySQL to generate a root password during its initialization. 
In this case we are generating a random password which you can find using `docker container logs <name>`.
<br>

When you open logs, locate `GENERATED ROOT PASSWORD` section to see your MySQL password.
<br>

You can also use `-e MYSQL_ALLOW_EMPTY_PASSWORD=yes` allowing to start MySQL container with an empty root password (not recommended for production environments) or `-e MYSQL_ROOT_PASSWORD=my_secret_password` to set a specific password of your choice.
<br>
<br>

After you run your containers this should be the output:
<br>

Open `http://localhost` in our web browser to check Nginx server.

![nginx](https://github.com/dinomite505/learning_docker/assets/131146683/646b7fd9-16d7-4315-a685-b2d55ba4f8b8)
<br>

- - - -
Open `http://localhost:8080` in your web browser to check your Apache server.

![apache2](https://github.com/dinomite505/learning_docker/assets/131146683/7ee2a177-a4bd-4fdd-a760-6be763207ab4)
<br>


- - - -
## Docker Networks :globe_with_meridians:

To **list** your networks:
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

### --network bridge
When we start a new container, and don't specify the network, it will automatically use the default virtual `bridge` network. Each container within bridge network gets its own IP address and they use Network Address Translation (NAT) configuration that maps container IP addresses to the host machine's IP address. Bridge network brings **isolation** from the host and other containers and container's **inter-communication**.
<br>

### --network host
Host network gains performance by skipping virtual networks and attaches the container **directly to the host interface**, rather than creating a separate network for the container. This means that the container shares the same network stack as the host machine making the container's network interface and ports directly accessible on the host's network. This **sacrifices security** of container model (prevents the security boundaries of the containerization from protecting the interface of that container).
<br>

### --network none
This option is used to completely **disable networking for a container**. If connected to it, the container has no network connectivity, it cannot communicate with the host, other containers or external networks. This is **useful for scenarios** where network access is not required and in security-sensitive cases where network must be restricted.
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

- - - -
## Connecting and Disconnecting Containers to/from Custom Networks 

`docker network connect` - dynamically creates a NIC in a container on an existing virtual network.
<br>

`docker network disconnect` - dynamically removes a NIC from a container on a specific virtual network
<br>
<br>

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
**USAGE:**`docker network connect <network_name_or_ID>`
<br>

```
docker network connect my_app_net proxy
```
```
docker network connect my_app_net webserver
```
```
docker network connect my_app_net db
```

<br>

To confirm you connected your containers to `my_app_net` you can use:

```
docker network inspect my_app_net
```

<br>

or to see to which network is your specific container connected to:

```
docker container inspect <container_ID>
```
<br>

- - - -
## Testing Container Ports :wrench:
<br>

### Nginx
```
$ curl localhost

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```
From the output we see the default welcome page of the Nginx web server. It indicates that Nginx is running and properly configured within our container.
<br>

- - - -
### Apache (HTTPD)
```
$ curl localhost:8080

<html><body><h1>It works!</h1></body></html>
```
Positive output from Apache server too.
<br>

INSERT PHOTO- SCREENSHOT; ISSUES; COMMIT NEW ISSUE; PASTE PHOTO; COPY CODE; EXIT; EDIT README; PASTE THE CODE
<br>

- - - -
### MySQL

Unlike Nginx and Apache which are web servers, to check if your MySQL server is running and accepting connections on your port you can use `Netcat` which is versatile and feature-rich networking utility that can handle a broader range of tasks, including bi-directional communication and file transfer. You can also use `Telnet` which is network protocol tool that allows you to establish text-based connections to remote services.
<br>
Here are both examples for our container:
```
nc -vz localhost 3306
```
```
telnet localhost 3306
```
If the MySQL server is running and accessible you will see a successful connection message.
```
Connection to localhost (127.0.0.1) 3306 port [tcp/mysql] succeeded!
```
<br>

To interact with the MySQL server and execute SQL queries you should use client like this:
```
mysql -h localhost -P 3306 -u root -p
```
:lock: You will then be prompted to enter the `RANDOM_ROOT_PASSWORD` you specified upon container's creation which you can find if you enter `docker container logs db`. If you used `ALLOW_EMPTY_PASSWORD` you will be logged in automatically as a root user.
<br>

After successful login you should get something like this:
```
WARNING: Forcing protocol to  TCP  due to option specification. Please explicitly state intended protocol.
Welcome to the MariaDB monitor.  Commands end with ; or \g.
MySQL connection id is 9
Server version: 8.1.0 MySQL Community Server - GPL
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
MySQL [(none)]> (to exit enter: **exit;**)
```
Meaning everything is working and you are now interacting with MySQL server using MariaDB monitor.
- - - -
## Cleaning Up :wastebasket:
#### Stopping Containers
To stop the containers use `docker container stop <container_name_or_ID>` so in our case we will use:
```
docker container stop proxy
```
You can stop containers individually or all at once by writing their names one after another like this:
```
docker container stop proxy webserver db
```
<br>

- - - -
#### Removing Containers
Stopped containers are not removed containers. Why remove stopped containers:
    
* They still consume valuable storage on your system
* It can pose security risks because its files are still in filesystem
* Containers are meant to be ephemeral and isolated
* Their temporary or orphaned files can create unnecessary clutter on your host system
* You may encounter conflict because of container names or IDs
<br>

For that matter we use:
```
docker container rm proxy webserver db
```
You can also remove **runnning** containers, but Docker doesn't allow that if you don't use **force** `-f` or `kill`. Both essentially do the same thing:
```
docker container rm -f <container_name_or_ID>
```
```
docker container kill <container_name_or_ID>
```
- - - -
#### Confirm Clean Space

To confirm that everything is clean you should use:
```
docker container ls -l
```
This command will show you both running and stopped containers if there's any.
<br>
<br>

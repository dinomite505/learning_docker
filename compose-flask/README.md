## Python/Flask application

Structure:

```
.
├── compose.yaml
├── app
    ├── app.py
    ├── Dockerfile
    └── requirements.txt

```

[_compose.yaml_](compose.yaml)

```
services:
  web:
    build:
      context: app
      target: builder
      # using SIGINT, when container is stopped, to send signal for Flask graceful shutdown
      # (default stop signal from Compose is SIGTERM)
    stop_signal: SIGINT
    ports:
      - '8000:8000'
```

## To deploy with docker compose

```
docker compose up -d
[+] Building 5.7s (11/11) FINISHED                                                                                                                                     docker:default
  ...

0.0s
 => => naming to docker.io/library/compose-flask-web                                                                                                         0.0s
[+] Running 2/2
 ✔ Network compose-flask_default  Created                                                                                                                    0.2s 
 ✔ Container compose-flask-web-1  Started                                                                                                                    0.0s
 ```

## Result

 Listing containers should show only one container running and the port mapping like below:

 ```
$ docker compose ps
NAME                  IMAGE               COMMAND            SERVICE   CREATED         STATUS         PORTS
compose-flask-web-1   compose-flask-web   "python3 app.py"   web       5 minutes ago   Up 5 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp
```

After the application starts open `http://localhost:8000` in your web browser or run:

```
$ curl localhost:8000
Hello World! This is Flask app
```

## Output screenshot

![flaskapp](https://github.com/dinomite505/learning_docker/assets/131146683/e1e4ab28-926e-4e62-8034-ab61d281cc31)

To stop and remove containers

```
$ docker compose down
[+] Running 2/2
 ✔ Container compose-flask-web-1  Removed                                                                                                                    0.5s 
 ✔ Network compose-flask_default  Removed
```

Good job!

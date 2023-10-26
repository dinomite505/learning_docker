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

## To deploy with compose

```
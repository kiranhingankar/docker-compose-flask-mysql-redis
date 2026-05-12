# Docker Compose Flask MySQL Redis Stack

Production-style multi-container application using Docker Compose with:

- Flask Web Application
- MySQL Database
- Redis Cache

This project demonstrates real-world Docker Compose concepts including:
- Multi-container orchestration
- Service dependencies
- Healthchecks
- Restart policies
- Named volumes
- Custom networks
- Scaling containers
- Custom Dockerfiles

---

# Architecture

```text
        ┌─────────────┐
        │   Browser   │
        └──────┬──────┘
               │
               ▼
        ┌─────────────┐
        │ Flask App   │
        │   (Web)     │
        └──────┬──────┘
               │
      ┌────────┴────────┐
      ▼                 ▼
┌────────────┐    ┌────────────┐
│   MySQL    │    │   Redis    │
│ Database   │    │   Cache    │
└────────────┘    └────────────┘
```

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Flask | Web application |
| MySQL | Relational database |
| Redis | In-memory cache |
| Python | Backend language |

---

# Project Structure

```bash
.
├── docker-compose.yml
├── README.md
│
└── app/
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

---

# Features

- Flask application containerized with Docker
- MySQL database with persistent storage
- Redis cache integration
- Healthchecks for database readiness
- `depends_on` with `service_healthy`
- Restart policies for resilience
- Custom Docker network
- Named Docker volumes
- Service labels for organization
- Horizontal scaling support

---

# Docker Compose Configuration

## Services

| Service | Description |
|---|---|
| flask_app | Flask web application |
| mysql_db | MySQL database |
| redis | Redis cache |

---

# Getting Started

## Prerequisites

Make sure Docker and Docker Compose are installed.

Verify installation:

```bash
docker --version
docker compose version
```

---

# Clone Repository

```bash
git clone https://github.com/your-username/docker-compose-flask-mysql-redis.git
cd docker-compose-flask-mysql-redis
```

---

# Start Application

## Build and Run Containers

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d --build
```

---

# Access Application

Open browser:

```text
http://localhost:5000
```

Expected response:

```text
MySQL + Redis Connected Successfully!
```

---

# Stop Application

```bash
docker compose down
```

---

# Healthchecks

The MySQL container includes a healthcheck to ensure the database is fully ready before the Flask app starts.

```yaml
healthcheck:
  test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-prootpass"]
  interval: 10s
  timeout: 5s
  retries: 5
```

---

# Restart Policies

This project demonstrates:

```yaml
restart: always
```

Benefits:
- Automatically restarts failed containers
- Improves service reliability
- Useful for production workloads

---

# Named Volumes

```yaml
volumes:
  mysql_data:
```

Purpose:
- Persistent MySQL storage
- Data survives container recreation

---

# Custom Networks

```yaml
networks:
  backend_nw:
```

Benefits:
- Isolated communication
- Better security
- Service discovery using container names

---

# Scaling Containers

Scale the web application:

```bash
docker compose up --scale web=3
```

## Important Note

Simple scaling with direct port mapping causes conflicts because multiple containers cannot bind to the same host port.

Production solutions:
- Nginx
- Traefik
- Kubernetes
- Docker Swarm

---

# Useful Commands

## View Running Containers

```bash
docker ps
```

---

## View Logs

```bash
docker compose logs -f
```

---

## Restart Containers

```bash
docker compose restart
```

---

## Remove Containers and Volumes

```bash
docker compose down -v
```

---

# Learning Outcomes

Through this project I learned:

- Multi-container application management
- Docker Compose networking
- Persistent storage with volumes
- Service dependency handling
- Healthchecks and readiness checks
- Container restart strategies
- Scaling limitations in Compose
- Production-style Docker workflows

---

# Future Improvements

- Add Nginx reverse proxy
- Add CI/CD pipeline
- Add monitoring with Prometheus & Grafana
- Add environment variable management using `.env`
- Deploy on Kubernetes

---

# Author

Kiran Hingankar

---

# Tags

`Docker` `Docker Compose` `Flask` `Redis` `MySQL` `DevOps` `Python` `Containers`

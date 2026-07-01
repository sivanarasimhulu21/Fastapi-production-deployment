# Book Catalog Deployment Project

A production-style backend deployment project using FastAPI, Docker, PostgreSQL, Redis, NGINX, and GitHub Actions.

---

# Features

- Add books
- View books
- Delete books
- PostgreSQL database integration
- Redis integration
- Dockerized services
- NGINX reverse proxy
- Health check endpoint
- CI/CD deployment workflow

---

# Tech Stack

- FastAPI
- PostgreSQL
- Redis
- Docker
- Docker Compose
- NGINX
- GitHub Actions
- AWS EC2

---

# Project Architecture

Internet
↓
NGINX
↓
FastAPI App
↓
PostgreSQL

FastAPI ↔ Redis

---

# Run Locally

## 1. Clone Repository

```bash
git clone <your-github-repo>
cd ai-notes-production-app
```

## 2. Create Environment File

```bash
cp .env.example .env
```

## 3. Start Containers

```bash
docker-compose up -d
```

---

# Access Application

## Application

http://localhost

## Health Check

http://localhost/health

---

# Docker Services

| Service | Purpose |
|---|---|
| FastAPI | Backend application |
| PostgreSQL | Database |
| Redis | Cache |
| NGINX | Reverse proxy |

---

# CI/CD Workflow

GitHub Actions automatically deploys the application to AWS EC2 when code is pushed to the main branch.

Workflow Steps:

1. Push code to GitHub
2. GitHub Actions starts workflow
3. SSH connection to EC2 server
4. Pull latest code
5. Restart Docker containers

---

# Security Measures

- Environment variables
- Reverse proxy using NGINX
- Firewall configuration
- SSH-based deployment
- Docker container isolation

---

# Backup Strategy

PostgreSQL backups can be created using:

```bash
pg_dump -U admin notesdb > backup.sql
```

---

# Health Check

Health endpoint:

```text
/health
```

Used for container monitoring and uptime verification.

---

# Future Improvements

- JWT Authentication
- HTTPS SSL setup
- Monitoring with Prometheus/Grafana
- Kubernetes deployment
- Automated backups

---

# Deployment

Deployed on AWS EC2 using Docker Compose.


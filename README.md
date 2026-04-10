# Flask System Health Dashboard

A self-hosted system monitoring dashboard built with Python and Flask,
containerised with Docker, and served via Nginx reverse proxy.
Currently being extended with PostgreSQL metric logging.

## Stack
- Python 3.11 + Flask
- Docker + Docker Compose
- Nginx (reverse proxy)
- PostgreSQL (metric logging) — in progress

## Architecture
[ Browser ]
↓
[ Nginx :80 ]        ← reverse proxy
↓
[ Flask :5000 ]      ← Python web app
↓
[ PostgreSQL ]       ← stores metric history

## Features
- Live CPU, RAM and disk usage displayed in browser
- Auto-refreshes on page reload
- Metrics logged to PostgreSQL on every visit
- Fully containerised via Docker Compose

## How to Run
```bash
git clone https://github.com/yourusername/flask-dashboard.git
cd flask-dashboard
docker-compose up -d
```

Then visit `http://<your-server-ip>` in your browser.

## Project Structure
flask-dashboard/
├── app/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── templates/
│       └── dashboard.html  # Frontend template
├── nginx/
│   └── nginx.conf          # Reverse proxy config
├── docker-compose.yml      # Multi-container orchestration
└── Dockerfile              # Container build instructions

## Environment Variables
| Variable | Description |
|---|---|
| DB_HOST | PostgreSQL host (default: postgres) |
| DB_NAME | Database name (default: metricsdb) |
| DB_USER | Database user |
| DB_PASSWORD | Database password |

## Part of
[Homelab DevOps Portfolio](https://github.com/yourusername) —
a hands-on Cloud/DevOps learning project built on Proxmox.

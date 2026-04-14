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

## What I Learned
- Writing a Python Flask web application from scratch
- Containerising a multi-service app with Docker Compose
- Configuring Nginx as a reverse proxy
- Connecting Flask to PostgreSQL using psycopg2
- Managing container networking and environment variables
- Debugging container startup race conditions

## Part of
[Homelab DevOps Portfolio](https://github.com/yourusername) —
a hands-on Cloud/DevOps learning project built on Proxmox.

## Deployment

### Local (Proxmox Homelab)
- Runs on Ubuntu Server 22.04 VM
- Accessible on home network via `http://<vm-ip>`

### Cloud (AWS EC2)
- Deployed to t3.micro EC2 instance in EU (London) region
- Ubuntu Server 22.04 LTS
- Publicly accessible via EC2 public IP
- Same Docker Compose stack as local deployment

## Backups

### S3 Log Backup
- PostgreSQL metrics table dumped hourly via cron
- Backup script uses AWS CLI to upload to S3
- Stored in `s3://your-bucket-name/backups/`
- Backup log stored at `/home/ubuntu/backup.log`

### How to Run Manually
```bash
bash backup.sh
```

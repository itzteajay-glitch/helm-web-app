# Helm Web App

This project provides a web interface to explore Helm and OCI repositories, fetch chart configurations, and generate HelmRelease YAML for Kubernetes.

## Features

- Explore Helm charts from a repository
- Dynamically configure chart values
- Generate HelmRelease YAML for FluxCD

## Setup

### Prerequisites

- Python 3.8+
- Node.js 14+
- Helm CLI

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm start
```

### Running with Docker Compose

```bash
docker-compose up
```

## Deploy

You can deploy this application using Kubernetes, Docker, or any cloud platform. Customize as needed!

# HealthCareHub Smart Healthcare Management Platform

## Installation
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
docker-compose build
npm run build
```

## Run
```bash
docker-compose up -d
uvicorn app.main:app --reload
npm start
```

## Dependencies
- FastAPI
- React
- PostgreSQL

## Usage
Start the servers and navigate to localhost:3000 to access the platform.

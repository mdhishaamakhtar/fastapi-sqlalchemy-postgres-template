<p align="center">
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FAST API"/>
<h2 align="center"> FastAPI Template </h2>
<h4 align="center"> A template for beginners </h4>

---
## About
This is a beginner-friendly template for getting started with FastAPI and SQLAlchemy.

## Features
- [x] Database connection using SQLAlchemy
- [x] FastAPI server
- [x] Unit testing with PyTest
- [x] Basic CRUD for posts

## Requirements
- Python 3.10+
- `pip`
- PostgreSQL database

## Setup
1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set environment variables:

| Key | Value |
| --- | --- |
| `DATABASE_URL` | `postgresql://user:password@host:port/db` |

Example (`.env`):

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_template
```

4. Run the API:

```bash
uvicorn main:app --reload
```

## API Docs (Swagger / OpenAPI)
Once the app is running locally, open:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## Running tests
```bash
pytest
```

## Formatting (Black)
Run formatter:

```bash
black .
```

## Docker (Local)
1. Create `.env` from example:

```bash
cp .env.example .env
```

2. Start API + Postgres with Docker Compose:

```bash
docker compose up --build
```

3. API will be available at:
- `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

`DATABASE_URL` is passed to the API container from `.env` through `docker-compose.yml`.

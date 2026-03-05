# FastAPI SQLAlchemy PostgreSQL Template

Minimal starter template for a CRUD API with FastAPI + SQLAlchemy + PostgreSQL.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Pytest](https://img.shields.io/badge/Pytest-9.0-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)

## Features

- FastAPI app with CORS enabled
- SQLAlchemy ORM integration
- Postgres-ready configuration via `DATABASE_URL`
- CRUD endpoints for `posts`
- Pytest suite (DB mocked for local test runs)
- Docker + Docker Compose local setup

## Requirements

- Python 3.10+
- `pip`
- PostgreSQL (only needed when running app without Docker)

## Local Setup (Without Docker)

1. Create and activate venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add env vars:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_template
```

4. Run API:

```bash
uvicorn main:app --reload
```

## API Docs

When the server is running:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## Tests

```bash
pytest
```

## Formatting

```bash
black .
```

## Docker (Recommended for Local Run)

1. Create `.env`:

```bash
cp .env.example .env
```

2. Build and start:

```bash
docker compose up --build
```

3. Access:

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

`DATABASE_URL` is passed to the API container from `docker-compose.yml` and can be overridden via `.env`.

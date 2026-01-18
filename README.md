Patient API

Simple in-memory patient management API using FastAPI.
Tech stack: Python, FastAPI, Pydantic, Uvicorn, Docker
Run locally: 

``
uvicorn app:app --reload
``

Or with Docker:

``
docker build -t patient-api .
``

``
docker run -p 8000:8000 patient-api
``

Test endpoints via Swagger UI: http://127.0.0.1:8000/docs

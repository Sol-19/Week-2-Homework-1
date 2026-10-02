# To-Do List API

A simple CRUD API for managing tasks, built with FastAPI. Data is stored in memory, so it resets when the server restarts.

## Run it

```
pip install "fastapi[standard]"
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs to try it in Swagger UI.

## Endpoints

- `POST /tasks` - create a task
- `GET /tasks` - list all tasks
- `GET /tasks/{id}` - get one task
- `PUT /tasks/{id}` - update a task
- `DELETE /tasks/{id}` - delete a task
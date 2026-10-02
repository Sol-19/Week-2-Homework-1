from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []
next_id = 1

class TaskIn(BaseModel):
    title: str
    done: bool = False

@app.get("/")
def root():
    return {"message": "hello"}

@app.post("/tasks", status_code = 201)
def create_task(task: TaskIn):
    global next_id
    new_task = {"id": next_id, "title": task.title, "done": task.done}
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.get("/tasks")
def list_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskIn):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated.title
            task["done"] = updated.done
            return task
    raise HTTPException(status_code=404, detail="Task not found")



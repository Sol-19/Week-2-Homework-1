from fastapi import FastAPI
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






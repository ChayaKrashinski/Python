from fastapi import FastAPI
from models.Task import Task

app=FastAPI()

tasks=[]

@app.get("/")
async  def root():
    return {"messege":"welcome!"}

@app.get("/{id}")
async def getTask(id:int):
    for t in tasks:
        if t.id == id:
            return  t
    return {"messege":"the task not found"}

@app.put("/")
async def getTask(task:Task):
    try:
        task = Task(**task)
        tasks.append(task)
    except ValueError as e:
        return{"status 400":e}

@app.post("/")
async def getTask(task:Task):
    try:
        task = Task(**task)
        for t in tasks:
            if t.id == task.id:
                t.descreption=task.descreption
                t.name = task.name
                t.status = task.status
                return{"messege": "the task updated"}
    except ValueError as e:
        return{"status 400":e}

@app.delete("/")
async def getTask(task:Task):
    try:
        task = Task(**task)
        tasks.remove(task)
    except ValueError as e:
        return{"status 400":e}

import uvicorn
if __name__ == '__main__':
    uvicorn.run("sample:app", host="127.0.0.1", port=8000, reload=True)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    summary: str
    description: str
    completed: bool
    
todo_db = []

@app.get('/todo')
def list_todo(summary: str = ""):
    print(f'Summary: {summary}')
    
    if summary != "":
        return [ task for task in todo_db if summary in task.summary ]
    
    return todo_db

@app.post('/todo', status_code=201)
def create_todo(todo: Todo):
    next_id = max([
        todo.id 
        for todo
        in todo_db
    ]) if len(todo_db) > 0 else 0
    
    next_id += 1
    
    todo.id = next_id
    todo_db.append(todo)
    
    return todo


@app.get('/todo/{todo_id}')
def get_todo(todo_id: int):
    found_todo = [
        todo
        for todo 
        in todo_db
        if todo.id == todo_id
    ]

    if len(found_todo) == 0:
        raise HTTPException(404, detail='Task not found')
    
    return found_todo[0]

@app.delete('/todo/{todo_id}', status_code=204)
def delete_task():
    pass
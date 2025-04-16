from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    id: int
    summary: str
    description: str
    completed: bool
    
todo_db = []



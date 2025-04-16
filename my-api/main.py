from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    active: bool

users_db = []

@app.get("/health")
def get_message():
    return {
        "healthy": "True"
    }

@app.get("/users")  
def list_users():
    return users_db

@app.post("/users", status_code = 201)
def create_user(user: User):
    next_id = max(
    [ 
        user.id 
        for user 
        in users_db
    ]) if len(users_db) > 0 else 0
    
    next_id += 1
    user.id = next_id

    users_db.append(user)
    
    return user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    found_users = [ 
        user 
        for user 
        in users_db 
        if user.id == user_id
    ]
    
    return found_users[0]
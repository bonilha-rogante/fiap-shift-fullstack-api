from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Referencia ao servidor
app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    active: bool
    
users_db = []

@app.get('/health')
def get_message():
    return {
        "healthy": "True"
    }
    
@app.get('/users')
def list_user():
    return users_db

@app.post('/users', status_code = 201)
def create_user(user: User):
    next_id = max(
        [ 
            user.id
            for user 
            in users_db 
        ] 
        ) if len(users_db) > 0 else 0 
    
    next_id += 1
    user.id = next_id
    users_db.append(user)
    
    return user

@app.get('/users/{user_id}')
def get_user(user_id: int):
    found_users = [ 
        user 
        for user 
        in users_db 
        if user.id == user_id 
    ]
    
    if len(found_users) == 0:
        raise HTTPException(404, detail="User not found")
    
    return found_users[0]

@app.delete('/users/{user_id}', status_code = 204)
def delete_user(user_id: int):
    global users_db
    
    found_users = [
        user 
        for user 
        in users_db 
        if user.id == user_id
    ]
    
    if len(found_users) == 0:
        raise HTTPException(
            404,
            detail='Unable to delete user, because it war not found'
        )
        
    users_db = [
        user 
        for user 
        in users_db 
        if user.id != user_id
    ]
    
    return None
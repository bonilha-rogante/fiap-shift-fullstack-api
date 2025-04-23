from fastapi import FastAPI

#Referencia ao servidor
app = FastAPI()

class User():
    id: int
    name: str
    active: bool
    
users_db = []

@app.get('/health')
def get_message():
    return {
        "healthy": "True"
    }
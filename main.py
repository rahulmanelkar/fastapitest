from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Testing API"}

@app.get("/{id}")
def root_id():
    return {"message":f"this is {id}"}
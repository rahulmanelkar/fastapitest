from fastapi import FastAPI
from pydantic import BaseModel
import numpy

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Testing API"}


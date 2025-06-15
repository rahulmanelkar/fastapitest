from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Testing API"}


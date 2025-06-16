from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import matplotlib

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Testing API"}


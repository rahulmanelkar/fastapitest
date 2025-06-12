from fastapi import FastAPI
from pydantic

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Testing API"}
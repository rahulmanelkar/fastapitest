from fastapi import FastAPI, Default
from pydantic import BaseModel
import numpy as np
import matplotlib as mp


app = FastAPI()

@app.get("/")
def root():
    return {"message":"Testing API"}


def main():
    pass

if __name__=='__main__':
    "API"
    main()


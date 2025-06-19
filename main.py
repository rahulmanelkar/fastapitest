from fastapi import FastAPI, Default
from pydantic import BaseModel
import numpy as np
import matplotlib


app = FastAPI()

@app.get("/")
def root():
    return {"message":"Testing API"}


def main():
    pass

if __name__=='__main__':


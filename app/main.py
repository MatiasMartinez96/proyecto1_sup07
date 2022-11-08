from fastapi import FastAPI
from netflix import dict19,dict20,dict21


app = FastAPI()

@app.get("/2019")
async def index():
    return dict19


@app.get("/2020")
async def index():
    return dict20


@app.get("/2021")
async def index():
    return dict21

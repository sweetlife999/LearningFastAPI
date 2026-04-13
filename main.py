from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/time")
async def get_time():
    return {"time": datetime.now().isoformat()}

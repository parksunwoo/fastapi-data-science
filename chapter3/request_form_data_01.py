from enum import Enum
from fastapi import FastAPI, Path, Query, Body, Form
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str

app = FastAPI()

@app.post("/users")
async def create_user(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}

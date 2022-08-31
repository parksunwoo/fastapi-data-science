from enum import Enum
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str

app = FastAPI()

@app.post("/users")
async def create_user(user: User, priority: int = Body(..., ge=1, le=3)):
    return {"user": user, "priority": priority}

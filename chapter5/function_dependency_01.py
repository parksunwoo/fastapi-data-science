from datetime import date
from typing import List, Dict, Optional, Tuple
from pydantic import BaseModel, validator
from enum import Enum

from fastapi import status, FastAPI, Header, Depends


app = FastAPI()


async def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
    return (skip, limit)


@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async  def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}



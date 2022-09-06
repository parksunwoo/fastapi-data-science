from datetime import date
from typing import List, Dict, Optional, Tuple
from pydantic import BaseModel, validator
from enum import Enum

from fastapi import status, FastAPI, Header, Depends, Query


app = FastAPI()


async def pagination(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async  def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}



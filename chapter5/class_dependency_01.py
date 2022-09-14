from datetime import date
from typing import List, Dict, Optional, Tuple
from enum import Enum

from pydantic import BaseModel, validator
from fastapi import status, FastAPI, Header, Depends, Query, HTTPException


app = FastAPI()


# async def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
#     return (skip, limit)

class Pagination:
    def __init__(self, maximum_limit: int =100):
        self.maximum_limit = maximum_limit

        async def __call__(
                self,
                skip: int = Query(0, ge=0),
                limit: int = Query(10, ge=0),
        ) -> Tuple[int, int]:
            capped_limit = min(self.maximum_limit, limit)
            return (skip, capped_limit)


pagination = Pagination(maximum_limit=50)


@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async  def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}



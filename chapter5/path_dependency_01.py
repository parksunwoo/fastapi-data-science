from datetime import date
from typing import List, Dict, Optional, Tuple
from enum import Enum

from pydantic import BaseModel, validator
from fastapi import status, FastAPI, Header, Depends, Query, HTTPException


app = FastAPI()


def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)


@app.get("/protected-route", dependencies=[Depends(secret_header)])
async def protected_route():
    return {"hello": "world"}


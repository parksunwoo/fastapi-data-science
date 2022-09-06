from datetime import date
from typing import List, Dict, Optional
from pydantic import BaseModel, validator
from enum import Enum
from fastapi import status, FastAPI, Header


app = FastAPI()


@app.get("/")
async def header(user_agent: str= Header(...)):
    return {"user_agent": user_agent}

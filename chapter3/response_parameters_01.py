

from fastapi import FastAPI, status, Response
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello": "world"}

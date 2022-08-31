

from fastapi import FastAPI, status, Response
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    return {"hello": "world"}

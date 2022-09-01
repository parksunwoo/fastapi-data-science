from fastapi import FastAPI, status, Response, Body, HTTPException
from fastapi.responses import  HTMLResponse, PlainTextResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    # nb_views: int

posts = {
    1: Post(title="hello", nb_views=100),
}

@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)

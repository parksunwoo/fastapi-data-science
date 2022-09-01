from os import path

from fastapi import FastAPI, status, Response, Body, HTTPException
from fastapi.responses import  HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    # nb_views: int

posts = {
    1: Post(title="hello", nb_views=100),
}

@app.get("/cat")
async def get_cat():
    root_directory = path.dirname(path.dirname(__file__))
    picture_path = path.join(root_directory, "assets", "cat.jpg")
    return FileResponse(picture_path)

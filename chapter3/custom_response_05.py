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

@app.get("/xml")
async def get_cat():
    content = """<?xml version="1.0" encoding="UTF-8"?>
        <Hello>World</Hello>
    """
    return Response(content=content, media_type="application/xml")

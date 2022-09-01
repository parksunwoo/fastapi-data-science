from fastapi import FastAPI, status, Response, Body, HTTPException
from fastapi.responses import  HTMLResponse, PlainTextResponse
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    # nb_views: int

posts = {
    1: Post(title="hello", nb_views=100),
}

@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Hello world!</title>
            </head>
            <body>
                <h1>Hello world!</h1>
            </body>
        </html>
    """


@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Hello world!"

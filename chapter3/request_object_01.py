from fastapi import FastAPI, File, UploadFile, Header, Cookie, Request
from typing import Dict, List, Set, Tuple, Optional

app = FastAPI()

@app.get("/")
async def get_request_object(request: Request):
    return {"path": request.url.path}

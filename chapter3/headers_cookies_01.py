from fastapi import FastAPI, File, UploadFile, Header
from typing import Dict, List, Set, Tuple

app = FastAPI()

@app.get("/")
async def get_header(hello: str = Header(...)):
    return {"hello": hello}

from fastapi import FastAPI, File, UploadFile, Header, Cookie
from typing import Dict, List, Set, Tuple, Optional

app = FastAPI()

@app.get("/")
async def get_cookie(hello: Optional[str] = Cookie(None)):
    return {"hello": hello}

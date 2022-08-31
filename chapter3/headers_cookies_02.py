from fastapi import FastAPI, File, UploadFile, Header
from typing import Dict, List, Set, Tuple

app = FastAPI()

@app.get("/")
async def get_header(user_agent: str = Header(...)):
    return {"user_agent": user_agent}

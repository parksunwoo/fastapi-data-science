from enum import Enum
from fastapi import FastAPI, Path, Query

class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"

app = FastAPI()

# @app.get("/users")
# async def get_user(page: int = 1, size: int = 10):
#     return {"page": page, "size": size}

# @app.get("/users")
# async def get_user(format: UsersFormat):
#     return {"format": format}

@app.get("/users")
async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}

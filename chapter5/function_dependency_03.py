from datetime import date
from typing import List, Dict, Optional, Tuple
from pydantic import BaseModel, validator
from enum import Enum

from fastapi import status, FastAPI, Header, Depends, Query, HTTPException


app = FastAPI()


async def get_post_or_404(id: int) -> Post:
    try
        return db.posts[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/posts/{id}")
async def get(post: Post = Depends(get_post_or_404)):
    return Post

@app.patch("/posts/{id}")
async def update(post_update: PostUpdate, post: Post= Depends(get_post_or_404)):
    updated_post = post.copy(update=post_update.dict())
    db.posts[post.id] = updated_post
    return updated_post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(post: Post = Depends(get_post_or_404)):
    db.posts.pop(post.id)










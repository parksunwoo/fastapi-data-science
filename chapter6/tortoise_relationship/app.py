from typing import List, Tuple

from fastapi import Depends, FastAPI, HTTPException, Query, status
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist

from chapter6.tortoise_relationship.models import (
    CommentBase,
    CommentDB,
    CommentTortoise,
    PostCreate,
    PostDB,
    PostPartialUpdate,
    PostPublic,
    PostTortoise,
)

app = FastAPI()


async def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_post_or_404(id: int) -> PostTortoise:
    try:
        return await PostTortoise.get(id=id).prefetch_related("comments")
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post("/comments", response_model=CommentDB, status_code=status.HTTP_201_CREATED)
async def create_comment(comment: CommentDB) -> CommentDB:
    try:
        await PostTortoise.get(id=comment.post_id)

    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Post {comment.post_id} does not exists",
        )

    comment_tortoise = await CommentTortoise.create(**comment.dict())

    return CommentDB.from_orm(comment_tortoise)


TORTOISE_ORM = {
    "connections": {"default": "sqlite://chapter6_tortoise_relationship.db"},
    "apps": {
        "models": {
            "models": ["chapter6.tortoise_relationship.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)
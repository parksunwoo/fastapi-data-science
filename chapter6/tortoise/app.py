from typing import List, Tuple

from fastapi import Depends, FastAPI, Query, status
from tortoise.contrib.fastapi import register_tortoise

from chapter6.tortoise.models import (
    PostDB,
    PostCreate,
    PostPartialUpdate,
    PostTortoise,
)

app = FastAPI()

TORTOISE_ORM = {
    "connection": {"default": "sqlite://chapter6_tortoise.db"},
    "apps": {
        "models": {
            "models": ["chapter6.tortoise.models"],
            "defalut_connection": "defalut",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


async def pagination(
        skip: int = Query(0, ge=0),
        limit: int = Query(0, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_post_or_404(id: int) -> PostTortoise:
    return await PostTortoise.get(id=id)


@app.post("/posts", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(
        post: PostCreate
) -> PostDB:
    post_tortoise = await PostTortoise.create(**post.dict())

    return PostDB.from_orm(post_tortoise)


@app.get("/posts")
async def list_posts(pagination: Tuple[int, int] = Depends(pagination)) -> List[PostDB]:
    skip, limit = pagination
    posts = await PostTortoise.all().offset(skip).limit(limit)
    results = [PostDB.from_orm(post) for post in posts]
    return results


@app.get("/posts/{id}", response_model=PostDB)
async def get_post(post: PostTortoise = Depends(get_post_or_404)) -> PostDB:
    return PostDB.from_orm(post)


@app.patch("/posts/{id}", response_model=PostDB)
async def update_post(
    post_update: PostPartialUpdate, post: PostTortoise = Depends(get_post_or_404)) -> PostDB:
    post.update_from_dict(post_update.dict(exclude_unset=True))
    await post.save()

    return PostDB.from_orm(post)


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post: PostTortoise = Depends(get_post_or_404)):
    await post.delete()


@app.post("/comments", response_model=CommentDB, status_code=status.HTTP_201_CREATED)
async def create_comments(
        comment: CommentCreate, database: Database = Depends(get_databse)
) -> CommentDB:
    select_post_query = posts.select().where(posts.c.id == comment.post_id)
    post = await database.fetch_one(select_post_query)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Post {comment.post_id} does not exist",
        )

    insert_query = comments.insert().values(comment.dict())
    comment_id = await database.execute(insert_query)

    select_query = comments.select().where(comments.c.id == comment_id)
    raw_comment = cast(Mapping, await database.fetch_one(select_query))

    return CommentDB(**raw_comment)




























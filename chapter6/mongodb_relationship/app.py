from typing import List, Tuple

from bson import ObjectId, errors
from fastapi import Depends, FastAPI, HTTPException, Query, status
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from chapter6.mongodb_relationship.models import (
    CommentCreate,
    PostDB,
    PostCreate,
    PostPartialUpdate,
)

app = FastAPI()
motor_client = AsyncIOMotorClient("mongodb://localhost:27017")
databse = motor_client["chapter6_mongo_relationship"]


def get_databse() -> AsyncIOMotorDatabase:
    return databse


async def pagination(
        skip: int = Query(0, ge=0),
        limit: int = Query(0, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except (errors.InvalidId, TypeError)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def get_post_or_404(
        id: ObjectId = Depends(get_object_id),
        database: AsyncIOMotorDatabase = Depends(get_databse)
) -> PostDB:
    raw_post = await database["posts"].find_one({"_id": id})

    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return PostDB(**raw_post)


@app.post("/posts", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(
        post: PostCreate, database: AsyncIOMotorDatabase = Depends(get_databse)
) -> PostDB:
    post_db = PostDB(**post.dict())
    await databse["posts"].insert_one(post_db.dict(by_alias=True))

    post_db = await get_post_or_404(post_db.id, database)

    return post_db


@app.get("/posts")
async def list_posts(
        pagination: Tuple[int, int] = Depends(pagination),
        database: AsyncIOMotorDatabase = Depends(get_databse)
) -> List[PostDB]:
    skip, limit = pagination
    query = database["posts"].find({}, skip=skip, limit=limit)
    results = [PostDB(**raw_post) async for raw_post in query]
    return results


@app.get("/posts/{id}", response_model=PostDB)
async def get_post(post: PostDB = Depends(get_post_or_404)) -> PostDB:
    return post


@app.patch("/posts/{id}", response_model=PostDB)
async def update_post(
    post_update: PostPartialUpdate,
    post: PostDB = Depends(get_post_or_404),
    database: AsyncIOMotorDatabase = Depends(get_databse)
) -> PostDB:
    await database["posts"].update_one(
        {"_id": post.id}, {"$set": post_update.dict(exclude_unset=True)}
    )

    post_db = await get_post_or_404(post.id, database)

    return post_db


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post: PostDB = Depends(get_post_or_404),
    databse: AsyncIOMotorDatabase = Depends(get_databse),
):
    await databse["posts"].delete_one({"_id": post.id})



@app.post("/posts/{id}/comments", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_comments(
        comment: CommentCreate,
        post: PostDB = Depends(get_post_or_404),
        database: AsyncIOMotorDatabase = Depends(get_databse),
) -> PostDB:
    await database["posts"].update_one(
        {"_id": post.id}, {"$push": {"comments": comment.dict()}}
    )
    post_db = await get_post_or_404(post.id, database)

    return post_db




























from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator
from tortoise.models import Model
from tortoise import fields


class CommentTortoise(Model):
    id = fields.IntField(pk=True, generated=True)
    post = fields.ForeignKeyField("models.PostTortoise", related_name="comments", null=False)
    publication_date = fields.DatetimeField(null=False)
    content = fields.TextField(null=False)

    class Meta:
        table = "comments"


class CommentBase(BaseModel):
    post_id: int
    publication_date: datetime = Field(default_factory=datetime.now)
    content: str

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    post_id: int
    publication_date: datetime = Field(default_factory=datetime.now)
    content: str

    class Config:
        orm_mode = True


class CommentDB(CommentBase):
    id: int


class PostBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True


class PostDB(PostBase):
    id: int


class PostPublic(PostDB):
    comments: List[CommentDB]

    @validator("comments", pre=True)
    def fetch_comments(cls, v):
        return list(v)













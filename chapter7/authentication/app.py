from typing import cast

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise import timezone
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist, IntegrityError

from chapter7.authentication.authentication import authenticate, create_access_token
from chapter7.authentication.models import (
    AccessTokenTortoise,
    User,
    UserCreate,
    UserDB,
    UserTortoise,
)
from chapter7.authentication.password import get_password_hash

app = FastAPI()

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate) -> User:
    hashed_password = get_password_hash(user.password)

    try:
        user_tortoise = await UserTortoise.create(
            **user.dict(), hashed_password=hashed_password
        )

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    return User.from_orm(user_tortoise)







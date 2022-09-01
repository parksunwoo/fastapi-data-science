from fastapi import FastAPI, status, Response, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    # nb_views: int

posts = {
    1: Post(title="hello", nb_views=100),
}

@app.post("/password")
async def check_password(password: str = Body(...), password_confirm: str = Body()):
    if password != password_confirm:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Passwords don't match.",
                "hints": [
                    "Check the caps lock on your keyboards", "Try to make the password",
                ],
            },
        )
    return {"message": "Passwords match."}

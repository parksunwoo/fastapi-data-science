import secrets

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecatd="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)



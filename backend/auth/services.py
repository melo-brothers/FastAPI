from datetime import datetime, timedelta, timezone

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from backend.settings import SECRET_KEY

from ..core.exceptions import get_user_exception
from .models import Users


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")
ALGORITHM = "HS256"


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def get_user(username: str, db):
    return db.query(Users).filter(Users.username == username).first()


def authenticate_user(username: str, password: str, db):
    if user := db.query(Users).filter(Users.username == username).first():
        return user if verify_password(password, user.hashed_password) else False
    else:
        return False


def create_access_token(username: str, user_id: int, expires_delta: timedelta | None = None):

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    encode = {"sub": username, "id": user_id, "exp": expire}
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if not username or not user_id:
            raise get_user_exception()
        return {"username": username, "id": user_id}
    except JWTError as e:
        raise get_user_exception() from e

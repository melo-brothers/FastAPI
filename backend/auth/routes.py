from datetime import timedelta

from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..core import get_db
from ..core.errors import raise_message
from ..core.exceptions import token_exception
from .exceptions import generic_exception
from .models import Users as TbUser
from .schemas import UserIn, UserOut
from .services import (
    authenticate_user,
    create_access_token,
    get_password_hash,
    get_user,
)


router = APIRouter(prefix="/auth", tags=["auth"], responses={status.HTTP_401_UNAUTHORIZED: {"user": "Not authorized"}})


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username, user.id, expires_delta=token_expires)
    return {"token": token}


create_new_user_info = dict(
    path="/create/user",
    description="Criação de usuários (atendentes) no sistema.",
    status_code=status.HTTP_201_CREATED,
    response_model=UserOut,
    response_description="Usuário criado com sucesso.",
)


@router.post(**create_new_user_info)
async def create_new_user(create_user: UserIn, response: Response, db: Session = Depends(get_db)):
    if user := get_user(create_user.username, db):
        raise raise_message(4002, name=user.username)
    try:
        user = TbUser()
        user.email = create_user.email
        user.username = create_user.username
        user.first_name = create_user.first_name
        user.last_name = create_user.last_name

        hash_password = get_password_hash(create_user.password)

        user.hashed_password = hash_password
        user.is_active = True

        db.add(user)
        db.commit()
    except Exception as e:
        raise generic_exception(e) from e
    else:
        response.status_code = status.HTTP_201_CREATED
        return user

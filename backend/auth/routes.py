from datetime import timedelta

from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..core import get_db
from ..core.exceptions import token_exception
from .exceptions import generic_exception
from .models import Users
from .schemas import CreateUser
from .services import authenticate_user, create_access_token, get_password_hash

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={status.HTTP_401_UNAUTHORIZED: {"user": "Not authorized"}}
)


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username,
                                user.id,
                                expires_delta=token_expires)
    return {"token": token}

@router.post("/create/user")
async def create_new_user(create_user: CreateUser, response: Response, db: Session = Depends(get_db)):
    try:
        create_user_model = Users()
        create_user_model.email = create_user.email
        create_user_model.username = create_user.username
        create_user_model.first_name = create_user.first_name
        create_user_model.last_name = create_user.last_name

        hash_password = get_password_hash(create_user.password)

        create_user_model.hashed_password = hash_password
        create_user_model.is_active = True

        db.add(create_user_model)
        db.commit()
    except Exception as e:
        raise generic_exception(e) from e
    else:
        response.status_code = status.HTTP_201_CREATED
        return create_user_model.json()

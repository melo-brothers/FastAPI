

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.auth.services import get_current_user, get_user_exception
from backend.core.database import get_db

from ..auth.models import Users as UsersModel
from .models import Address as AddressModel
from .schemas import Address as AddressSchema

router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not found"}}
)


@router.post("/")
async def create_address(address: AddressSchema,
                         user: dict = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    address_model = AddressModel()
    address_model.address1 = address.address1
    address_model.address2 = address.address2
    address_model.city = address.city
    address_model.state = address.state
    address_model.country = address.country
    address_model.postalcode = address.postalcode

    db.add(address_model)
    db.flush()

    user_model = db.query(UsersModel).filter(UsersModel.id == user.get("id")).first()

    user_model.address_id = address_model.id

    db.add(user_model)

    db.commit()









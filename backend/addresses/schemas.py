from pydantic import BaseModel


class Address(BaseModel):
    address1: str
    address2: str | None = None
    city: str
    state: str
    country: str
    postalcode: str

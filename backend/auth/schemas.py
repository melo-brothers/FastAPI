from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    email: str | None = None


class UserOut(BaseModel):
    id: int
    username: str
    email: str | None = None

    class Config:
        orm_mode = True

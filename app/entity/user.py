from sqlmodel import SQLModel


class BaseUser(SQLModel):
    name: str
    email: str
    phone: str


class InputUser(BaseUser):
    pass


class User(BaseUser):
    id: int | None

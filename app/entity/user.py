from pydantic import BaseModel


class User(BaseModel):
    id: int | None
    name: str
    email: str
    phone: str

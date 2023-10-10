from pydantic import BaseModel

from app.entity.user import User


class BaseAdventure(BaseModel):
    user: User
    location: str
    status: str  # before | started | returned | contacted


class Adventure(BaseAdventure):
    id: int

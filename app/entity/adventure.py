from entity.user import User
from pydantic import BaseModel


class BaseAdventure(BaseModel):
    user: User
    location: str
    status: str  # before | started | returned | contacted


class Adventure(BaseAdventure):
    id: int

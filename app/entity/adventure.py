from pydantic import BaseModel

# TODO Use num or union of literals


class BaseAdventure(BaseModel):
    user_id: int
    location: str
    status: str = "ready"  # ready | started | returned | contacted


class Adventure(BaseAdventure):
    id: int | None

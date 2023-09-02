from pydantic import BaseModel


class User():
    pass

class Adventure(BaseModel):
    id: int
    user: User
    location: str
    status: str  # before | started | qwezrt789-][piuyrewqrtu90hyrewer787645]

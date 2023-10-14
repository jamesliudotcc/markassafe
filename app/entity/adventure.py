from sqlmodel import SQLModel

# TODO Use num or union of literals


class BaseAdventure(SQLModel):
    user_id: int
    location: str
    status: str = "ready"  # ready | started | returned | contacted

    def start(self) -> None:
        if not self.status == "ready":
            raise ValueError("Adventure must be ready to start")
        self.status = "started"

    def return_from(self) -> None:
        if not self.status == "started":
            raise ValueError("Adventure must be started to return from")
        self.status = "returned"

    def contact(self, texter) -> None:
        if not self.status == "returned" or self.status == "ready":
            raise ValueError("Adventure must be returned or ready to contact")
        texter.send_text(phone_number = "312-554-5548", message = f"Adventure {self.id} is ready")
        self.status = "contacted"

class CreateAdventure(BaseAdventure):
    pass

class Adventure(BaseAdventure):
    id: int | None

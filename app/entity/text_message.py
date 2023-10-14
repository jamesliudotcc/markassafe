from pydantic import BaseModel


class BaseTextMessage(BaseModel):
    user_id: int
    message: str
    status: str = "draft" # "draft" | "sent" | "acked"

    def send_text(self, message: str, phone_number: str):
        raise NotImplementedError

class TextMessage(BaseTextMessage):
    def send_text(self, message: str, phone_number: str):
        print(f"Sending text message: {message} to number: {phone_number}")
        self.status = "sent"
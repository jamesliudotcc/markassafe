from abc import ABC, abstractmethod


class AbstractTexter(ABC):
    @abstractmethod
    def send_text(self, message: str, phone_number: str):
        """Send a text message."""
        raise NotImplementedError
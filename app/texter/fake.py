from .abstract import AbstractTexter


class FakeTexter(AbstractTexter):
    def send_text(self, phone_number, message):
        print(f"Sending fake text: {message} to number: {phone_number}")

fake_texter = FakeTexter()
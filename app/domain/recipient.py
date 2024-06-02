
class Recipient:

    def __init__(self, email: str):
        self._email = email

    @property
    def email(self):
        return self._email

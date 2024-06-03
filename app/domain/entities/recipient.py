
class Recipient:

    def __init__(self, email: str):
        self._email = email

    def __eq__(self, other: 'Recipient'):
        return self._email == other._email

    @property
    def email(self) -> str:
        return self._email

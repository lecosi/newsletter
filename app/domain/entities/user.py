

class User:

    def __init__(self, id: str, username: str, password: str, is_admin: bool):
        self._id = id
        self._username = username
        self._password = password
        self._is_admin = is_admin

    @property
    def id(self) -> str:
        return self._id

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def is_admin(self) -> str:
        return self._is_admin

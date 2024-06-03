
import sqlite3
from typing import Optional


from app.configuration import config
from app.domain.entities.user import User
from app.domain.repositories import UserRepository


class SqliteUserRepository(UserRepository):
    def __init__(self):
        self._database_path = config.get_settings().DATABASE_URL

    def add(self, user: User):
        connection = sqlite3.connect(str(self._database_path))
        connection.execute(
            "insert into users (id, username, password, is_admin) "
            "values (?, ?, ?, ?)",
            (
                user._id,
                user.username,
                user.password,
                user.is_admin
            )
        )
        connection.commit()
        connection.close()

    def get_by_id(self, id: str) -> Optional[User]:
        connection = sqlite3.connect(str(self._database_path))
        cursor = connection.cursor()
        cursor.execute(
            'select id, username, is_admin '
            'from subscriptions where id = ?',
            (id,)
        )
        row = cursor.fetchone()
        connection.close()
        return Subscription(
            id=row[0],
            newsletter=row[1],
            recipient_list=row[2]
        )

import sqlite3
from typing import Optional, List

from app.configuration import config
from app.domain.entities import Newsletter
from app.domain.repositories import NewsletterRepository


class SqliteNewsletterRepository(NewsletterRepository):

    def __init__(self):
        self._database_path = config.get_settings().DATABASE_URL

    def add(self, newsletter: Newsletter) -> None:

        if newsletter.file:
            file = newsletter.file.filename
        else:
            file = None

        connection = sqlite3.connect(str(self._database_path))
        connection.execute(
            "insert into newsletters (id, name, file_path) values (?, ?, ?)",
            (
                newsletter.id,
                newsletter.name,
                file

            )
        )
        connection.commit()
        connection.close()

    def get_by_id(self, id: str) -> Optional[Newsletter]:
        connection = sqlite3.connect(str(self._database_path))
        cursor = connection.cursor()
        cursor.execute(
            'select id, name from newsletters where id = ?',
            (id,)
        )
        row = cursor.fetchone()
        connection.close()
        return Newsletter(
            id=row[0],
            name=row[1],
            file=None
        )

    def get_all(self) -> Optional[List[Newsletter]]:
        connection = sqlite3.connect(str(self._database_path))
        cursor = connection.cursor()
        cursor.execute(
            'select id, name from newsletters',
        )
        rows = cursor.fetchall()
        connection.close()
        return [Newsletter(id=row[0], name=row[1], file=None) for row in rows]

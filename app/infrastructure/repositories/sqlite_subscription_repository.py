
import sqlite3
from typing import Optional


from app.configuration import config
from app.domain.entities import Subscription, Newsletter, Recipient
from app.domain.repositories import SubscriptionRepository


class SqliteSubscriptionRepository(SubscriptionRepository):
    def __init__(self):
        self._database_path = config.get_settings().DATABASE_URL

    def add(self, subscription: Subscription):
        connection = sqlite3.connect(str(self._database_path))
        connection.execute(
            "insert into subscriptions (id, newsletter_id, recipients) "
            "values (?, ?, ?)",
            (
                subscription.id,
                subscription.newsletter.id,
                ','.join(map(
                    lambda recipient: recipient.email,
                    subscription.recipients)
                )
            )
        )
        connection.commit()
        connection.close()

    def get_by_id(self, id: str) -> Optional[Subscription]:
        connection = sqlite3.connect(str(self._database_path))
        cursor = connection.cursor()
        cursor.execute(
            '''
                select
                    s.id,
                    s.newsletter_id,
                    s.recipients,
                    n.id,
                    n.name
                from subscriptions as s
                join newsletters as n on (n.id = s.newsletter_id)
                where s.id = ?
            ''',
            (id,)
        )
        row = cursor.fetchone()
        connection.close()
        return Subscription(
            id=row[0],
            newsletter=Newsletter(id=row[3], name=row[4]),
            recipients=[
                Recipient(email=email) for email in row[2].split(',')
            ]
        )

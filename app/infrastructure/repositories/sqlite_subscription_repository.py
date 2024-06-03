
import sqlite3
import uuid
from typing import Optional, List

from app.configuration import config
from app.domain.entities import Subscription, Newsletter, Recipient
from app.domain.repositories import SubscriptionRepository


class SqliteSubscriptionRepository(SubscriptionRepository):

    def __init__(self):
        self._database_path = config.get_settings().DATABASE_URL

    def add(self, subscription: Subscription):
        connection = sqlite3.connect(str(self._database_path))
        values = []
        for recipient in subscription.recipients:
            values.append((
                str(uuid.uuid4()),
                subscription.newsletter.id,
                recipient.email
            ))

        connection.executemany(
            "insert into subscriptions (id, newsletter_id, recipient_id) "
            "values (?, ?, ?)",
            values
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

    def get_by_newsletter_id(self, newsletter_id) -> Optional[Subscription]:
        connection = sqlite3.connect(str(self._database_path))
        cursor = connection.cursor()
        cursor.execute(
            '''
                select
                    s.newsletter_id,
                    s.recipient_id,
                    n.id,
                    n.name
                from subscriptions as s
                join newsletters as n on (n.id = s.newsletter_id)
                where s.newsletter_id = ?
            ''',
            (newsletter_id,)
        )
        rows = cursor.fetchall()
        connection.close()
        recipients = []
        for i, row in enumerate(rows):
            recipients.append(Recipient(email=row[1]))

        return Subscription(
            newsletter=Newsletter(id=rows[0][2], name=rows[0][3]),
            recipients=recipients
        )

    def delete_subscription_by_recipient_email(self, recipient_email: str):
        connection = sqlite3.connect(str(self._database_path))
        cursor = connection.cursor()
        cursor.execute(
            """
                delete  
                from subscriptions
                where recipient_id = '?'
            """,
            (recipient_email, )
        )
        connection.close()

import uuid

from app.domain.entities import Recipient, Subscription, Newsletter
from app.infrastructure.mailing.mailjet_mailing_service import \
    MailjetMailingService


def test_send_without_attachment():
    mailjet_service = MailjetMailingService()

    was_sent = mailjet_service.send(
        Subscription(
            recipients=[
                Recipient('test@test@com'), Recipient('test1@test@com'),
            ],
            newsletter=Newsletter(
                id=str(uuid.uuid4()),
                name='Boletin',
                file=None
            )
        )
    )

    assert was_sent is True

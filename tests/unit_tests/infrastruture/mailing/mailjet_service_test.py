from app.domain.entities import Recipient
from app.infrastructure.mailing.mailjet_mailing_service import \
    MailjetMailingService


def test_send_without_attachment():
    mailjet_service = MailjetMailingService()

    was_sent = mailjet_service.send(
        (
            Recipient('test@test@com'),
            Recipient('test1@test@com'),
        )
    )

    assert was_sent is True

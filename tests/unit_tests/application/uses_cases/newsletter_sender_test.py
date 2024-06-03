from unittest.mock import MagicMock

from app.application.use_cases import Subscriber, NewsletterSender


def test_send(newsletter_fixture, newsletter_repository, subscription_repository):
    email_addresses = ['test@test.com']
    subscriber = Subscriber(
        newsletter_id=newsletter_fixture.id,
        newsletter_repository=newsletter_repository,
        subscription_repository=subscription_repository,
        email_addresses=email_addresses
    )
    subscriber.subscribe()
    mailing_service = MagicMock()
    mailing_service.send.return_value = True
    newsletter_sender = NewsletterSender(
        newsletter_id=newsletter_fixture.id,
        mailing_service=mailing_service,
        subscription_repository=subscription_repository
    )

    was_sent = newsletter_sender.send()

    mailing_service.send.assert_called_once()
    assert was_sent is True



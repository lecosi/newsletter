import uuid

from app.domain.entities import Subscription, Newsletter, Recipient
from app.infrastructure.repositories import SqliteNewsletterRepository, \
    SqliteSubscriptionRepository


def test_get_by_id(create_db):
    newsletter = Newsletter(name="test", id=str(uuid.uuid4()))
    repository = SqliteNewsletterRepository()
    repository.add(newsletter)
    repository = SqliteSubscriptionRepository()
    recipients = [Recipient(email='test@test.com')]
    subscription = Subscription(
        newsletter=newsletter,
        id=str(uuid.uuid4()),
        recipients=recipients
    )
    repository.add(subscription)

    fetched_subscription = repository.get_by_id(subscription.id)

    assert fetched_subscription == subscription
    assert fetched_subscription.recipients == subscription.recipients

import uuid
from typing import Collection

from app.domain.entities import Subscription, Recipient
from app.domain.repositories import SubscriptionRepository, \
    NewsletterRepository


class Subscriber:

    def __init__(self, email_addresses: Collection[str], newsletter_id: str,
                 subscription_repository: SubscriptionRepository,
                 newsletter_repository: NewsletterRepository):
        self._email_addresses = email_addresses
        self._newsletter_id = newsletter_id
        self._subscription_repository = subscription_repository
        self._newsletter_repository = newsletter_repository

    def subscribe(self) -> Subscription:
        newsletter = self._newsletter_repository.get_by_id(self._newsletter_id)
        subscription = Subscription(
            recipients=[
                Recipient(email=email) for email in self._email_addresses
            ],
            newsletter=newsletter
        )
        self._subscription_repository.add(subscription)
        return subscription

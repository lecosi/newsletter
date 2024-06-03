
from app.domain.repositories import SubscriptionRepository


class Unsubscriber:
    def __init__(self, recipient_email: str,
                 subscription_repository: SubscriptionRepository):
        self._recipient_email=recipient_email
        self._subscription_repository = subscription_repository

    def unsubscribe(self):
        self._subscription_repository.\
            delete_subscription_by_recipient_email(
                recipient_email=self._recipient_email
            )

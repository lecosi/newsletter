from app.domain.mailing_service import MailingService
from app.domain.repositories import SubscriptionRepository


class NewsletterSender:

    def __init__(self, newsletter_id: str, mailing_service: MailingService,
                 subscription_repository: SubscriptionRepository):
        self._newsletter_id = newsletter_id
        self._mailing_service = mailing_service
        self._subscription_repository = subscription_repository

    def send(self) -> bool:
        subscription = self._subscription_repository.get_by_newsletter_id(
            self._newsletter_id
        )
        if not subscription:
            return False

        return self._mailing_service.send(subscription)

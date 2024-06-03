from typing import Optional

from pydantic import BaseModel

from app.domain.repositories import SubscriptionRepository
from app.domain.repositories import NewsletterRepository


class StatisticDataModel(BaseModel):
    total_newsletter: int = 0
    total_subscribers: int = 0


class Statistic:

    def __init__(self, newsletter_repository: NewsletterRepository,
                 subscription_repository: SubscriptionRepository):

        self._newsletter_repository = newsletter_repository
        self._subscription_repository = subscription_repository

    def get(self) -> Optional[StatisticDataModel]:
        newsletter_count = len(self._newsletter_repository.get_all())
        #subscriptions = self._subscription_repository.get_all()
        total_subcribers = 0

        return StatisticDataModel(
            total_newsletter=newsletter_count,
            total_subscribers=total_subcribers
        )

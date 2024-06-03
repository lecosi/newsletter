from abc import ABC, abstractmethod
from typing import Optional, List

from app.domain.entities import Newsletter, Subscription


class NewsletterRepository(ABC):

    @abstractmethod
    def add(self, newsletter: Newsletter):
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Newsletter]:
        pass

    @abstractmethod
    def get_all(self) -> Optional[List[Newsletter]]:
        pass


class SubscriptionRepository(ABC):

    @abstractmethod
    def add(self, subscription: Subscription):
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Subscription]:
        pass

    @abstractmethod
    def get_by_newsletter_id(self, newsletter_id) -> Optional[Subscription]:
        pass

    @abstractmethod
    def delete_subscription_by_recipient_email(
        self,
        recipient_email: str
    ):
        pass

from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities import Newsletter, Subscription


class NewsletterRepository(ABC):

    @abstractmethod
    def add(self, newsletter: Newsletter):
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[Newsletter]:
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

# class UserRepository(ABC):
#
#     @abstractmethod
#     def add(self, user: User):
#         pass
#
#     @abstractmethod
#     def get_by_id(self, id: str) -> Optional[User]:
#         pass

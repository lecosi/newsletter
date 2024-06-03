from abc import ABC, abstractmethod
from typing import Collection

from app.domain.entities import Recipient, Subscription


class MailingService(ABC):

    @abstractmethod
    def send(self, subscription: Subscription) -> bool:
        pass

from abc import ABC, abstractmethod
from typing import Collection

from app.domain.entities import Recipient


class MailingService(ABC):

    @abstractmethod
    def send(self, recipients: Collection[Recipient]) -> bool:
        pass

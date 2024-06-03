from typing import List

from app.domain.entities import Newsletter
from app.domain.entities.recipient import Recipient


class Subscription:

    def __init__(self, id: str, newsletter: Newsletter,
                 recipients: List[Recipient]):
        self._id = id
        self._newsletter = newsletter
        self._recipients = recipients

    def __eq__(self, other: 'Subscription'):
        return self._id == other._id

    @property
    def id(self):
        return self._id

    @property
    def newsletter(self):
        return self._newsletter

    @property
    def recipients(self):
        return self._recipients
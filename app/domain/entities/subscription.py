from typing import List, Optional

from app.domain.entities import Newsletter
from app.domain.entities.recipient import Recipient


class Subscription:

    def __init__(self, recipients: List[Recipient],
                 newsletter: Optional[Newsletter] = None):
        self._newsletter = newsletter
        self._recipients = recipients

    def __eq__(self, other: 'Subscription'):
        return self._newsletter.id == other._newsletter.id

    @property
    def newsletter(self):
        return self._newsletter

    @property
    def recipients(self):
        return self._recipients
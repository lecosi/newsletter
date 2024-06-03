from typing import Optional, List

from app.domain.entities import Newsletter
from app.domain.repositories import NewsletterRepository


class NewsletterGetListData:

    def __init__(self, newsletter_repository: NewsletterRepository):
        self._newsletter_repository = newsletter_repository

    def get_all(self) -> List[Newsletter]:
        return self._newsletter_repository.get_all()

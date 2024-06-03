import uuid
from typing import Optional

from app.domain.entities import Newsletter
from app.domain.repositories import NewsletterRepository


class NewsletterCreator:

    def __init__(self, newsletter_name: str,
                 newsletter_repository: NewsletterRepository):
        self._newsletter_name = newsletter_name
        self._newsletter_repository = newsletter_repository

    def create(self) -> Optional[Newsletter]:
        newsletter = Newsletter(
            id=str(uuid.uuid4()),
            name=self._newsletter_name
        )
        self._newsletter_repository.add(newsletter=newsletter)
        return newsletter

from app.domain.newsletter_repository import NewsletterRepository


class UserSubscriber:

    def __init__(self, email: str, newsletter_repository: NewsletterRepository):
        self._email = email
        self._repository = newsletter_repository

    def subscribe(self):
        pass

from app.domain.newsletter import Newsletter
from app.domain.newsletter_repository import NewsletterRepository


class PostgresNewsletterRepository(NewsletterRepository):
    def save(self, newsletter: Newsletter):
        pass

from app.application.user_subscriber import UserSubscriber
from app.infrastructure.repositories.postgres_newsletter_repository import \
    PostgresNewsletterRepository


def handler():
    user_subscriber = UserSubscriber(
        email='oeuaoeu',
        newsletter_repository=PostgresNewsletterRepository()
    )
    user_subscriber.subscribe()


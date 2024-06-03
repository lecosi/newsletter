from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.application.use_cases import Subscriber
from app.infrastructure.api.schemas.newsletter_schema import \
    InputSendNewsletterModel
from app.infrastructure.repositories import SqliteSubscriptionRepository, \
    SqliteNewsletterRepository

router = APIRouter()


@router.post('/send')
def send_newsletter(message_data: InputSendNewsletterModel):
    return {"message": "Hello World"}


class SubscriptionBody(BaseModel):
    email_recipients: list[str]
    newsletter_id: str


@router.post('/subscription')
def subscribe_handler(request: Request, subscription_body: SubscriptionBody):
    subscriber = Subscriber(
        newsletter_id=subscription_body.newsletter_id,
        email_addresses=subscription_body.email_recipients,
        subscription_repository=SqliteSubscriptionRepository(),
        newsletter_repository=SqliteNewsletterRepository()
    )
    subscriber.subscribe()
    return {}

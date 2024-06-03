from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.application.use_cases import Subscriber, NewsletterSender
from app.infrastructure.api.schemas.newsletter_schema import \
    InputSendNewsletterModel
from app.infrastructure.mailing.mailjet_mailing_service import \
    MailjetMailingService
from app.infrastructure.repositories import SqliteSubscriptionRepository, \
    SqliteNewsletterRepository

router = APIRouter()


@router.post('/send')
async def send_newsletter(request: Request):
    body = await request.json()
    newsletter_sender = NewsletterSender(
        newsletter_id=body.get('newsletter_id'),
        subscription_repository=SqliteSubscriptionRepository(),
        mailing_service=MailjetMailingService()
    )
    return {'ok': newsletter_sender.send()}


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

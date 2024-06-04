from typing import Annotated

from fastapi import APIRouter, Request, UploadFile, Form, File, HTTPException
from pydantic import BaseModel

from app.application.use_cases import Subscriber, NewsletterSender, \
    Unsubscriber
from app.application.use_cases.newsletter_creator import NewsletterCreator
from app.application.use_cases.newsletter_get_data import NewsletterGetListData
from app.infrastructure.mailing.mailjet_mailing_service import \
    MailjetMailingService
from app.infrastructure.repositories import SqliteSubscriptionRepository, \
    SqliteNewsletterRepository

router = APIRouter()


@router.post('/', status_code=201)
def create_newsletter(
    name: Annotated[str, Form()],
    recipients: Annotated[str, Form()],
    document_file: Annotated[UploadFile, File()] = None,

):
    formatted_recipients = recipients.strip().split(',')
    newsletter_creator = NewsletterCreator(
        newsletter_name=name,
        document_file=document_file,
        newsletter_repository=SqliteNewsletterRepository()
    )
    newsletter = newsletter_creator.create()
    subscriber = Subscriber(
        newsletter_id=newsletter.id,
        email_addresses=formatted_recipients,
        subscription_repository=SqliteSubscriptionRepository(),
        newsletter_repository=SqliteNewsletterRepository()
    )
    subscriber.subscribe()

    return {
        'id': newsletter.id,
        'name': newsletter.name
    }


@router.get('/', status_code=200)
def get_newsletter_list():
    newsletter_get_data = NewsletterGetListData(
        newsletter_repository=SqliteNewsletterRepository()
    )
    return newsletter_get_data.get_all()


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


@router.get('/unsubscription/{email_recipient}')
def unsubscribe_handler(email_recipient):
    try:
        subscriber = Unsubscriber(
            recipient_email=email_recipient,
            subscription_repository=SqliteSubscriptionRepository(),
        )
        subscriber.unsubscribe()
    except Exception:
        return HTTPException(
            status_code=500,
            detail='Error unsubscription email'
        )
    return {'unsubscription': True}

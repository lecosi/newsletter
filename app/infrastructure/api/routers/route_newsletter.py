from fastapi import APIRouter

from app.infrastructure.api.schemas.newsletter_schema import \
    InputSendNewsletterModel

router = APIRouter()


@router.post('/send')
def send_newsletter(message_data: InputSendNewsletterModel):
    return {"message": "Hello World"}

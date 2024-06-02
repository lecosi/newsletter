
from pydantic import BaseModel


class RecipientMailModel(BaseModel):
    Email: str
    Name: str = None


class InputSendNewsletterModel(BaseModel):
    recipient_list: list[RecipientMailModel]
    document_file: str = None


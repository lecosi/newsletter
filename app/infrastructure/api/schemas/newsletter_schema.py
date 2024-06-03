from typing import Optional

from pydantic import BaseModel, field_validator


class RecipientMailModel(BaseModel):
    email: str
    name: str = None


class InputSendNewsletterModel(BaseModel):
    recipient_list: list[RecipientMailModel]
    category_name: str
    document_file: str = None

    @field_validator("category_name")
    @classmethod
    def validate_name(cls, category_name: str) -> Optional[str]:
        if category_name.isdigit():
            raise ValueError('category name must have letters')

        return category_name.upper()



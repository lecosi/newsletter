import logging
from tempfile import TemporaryFile
import uuid
from typing import Optional, Union

from fastapi import HTTPException

from app.domain.entities import Newsletter
from app.domain.repositories import NewsletterRepository

logger = logging.getLogger(__name__)


class NewsletterCreator:

    def __init__(self, newsletter_name: str,
                 newsletter_repository: NewsletterRepository,
                 document_file: Union[TemporaryFile, None] = None):
        self._document_file = document_file
        self._newsletter_name = newsletter_name
        self._newsletter_repository = newsletter_repository

    def create(self) -> Optional[Newsletter]:
        newsletter = Newsletter(
            id=str(uuid.uuid4()),
            name=self._newsletter_name,
            file=self._document_file
        )
        self._newsletter_repository.add(newsletter=newsletter)
        self._upload_file()
        return newsletter

    def _upload_file(self):
        if not self._document_file:
            return

        try:
            folder = "app/infrastructure/statics"
            file_path = f"{folder}/{self._document_file.filename}"
            with open(file_path, "wb") as f:
                f.write(self._document_file.file.read())
                print('ok')
        except Exception as e:
            logger.error(f'create_newsletter :: {e}')
            return HTTPException(status_code=500, detail='Error upload file')

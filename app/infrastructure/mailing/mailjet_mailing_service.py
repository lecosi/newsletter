from typing import Collection

import requests

from app.configuration import config
from app.domain.entities import Recipient
from app.domain.mailing_service import MailingService


class MailjetMailingService(MailingService):

    def send(self, recipients: Collection[Recipient]) -> bool:
        settings = config.get_settings()
        data = {
            'FromEmail': settings.MAILJET_DEFAULT_EMAIL,
            'FromName': "Boletin",
            'Recipients': [
                {'Email': recipient.email for recipient in recipients}
            ],
            'Subject': 'test',
            'Html-part': '',
            'SandboxMode': True
        }
        response = requests.post(
            settings.MAILJET_API_URL,
            auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY),
            headers={'Accept': 'application/json'},
            json=data
        )
        return response.ok

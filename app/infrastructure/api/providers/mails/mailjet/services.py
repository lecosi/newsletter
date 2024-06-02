from typing import List, Dict

from app.configuration.config import settings
from app.infrastructure.api.utils.rest_api_client import RestAPIClient


class MailJetService:

    def __init__(self):
        self._client = RestAPIClient()
        self._headers = {'Accept': 'application/json'}

    def send_message(
        self,
        subject: str,
        template_html: str,
        recipient_email_list: List[Dict[str, str]],
        document_file: str = None
    ) -> bool:
        auth = (settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY)
        data = {
            'FromEmail': settings.MAILJET_DEFAULT_EMAIL,
            'FromName': "Boletin",
            'Recipients': recipient_email_list,
            'Subject': subject,
            'Html-part': template_html
        }
        if document_file:
            data['file'] = [("attachment", document_file)]

        response = self._client.request_post(
            url=settings.MAILJET_API_URL,
            headers=self._headers,
            auth=auth,
            data=data
        )

        return response.json()

import base64

import requests
from jinja2 import Environment, FileSystemLoader

from app.configuration import config
from app.domain.entities import Subscription
from app.domain.mailing_service import MailingService


class MailjetMailingService(MailingService):

    def send(self, subscription: Subscription) -> bool:
        settings = config.get_settings()
        file = subscription.newsletter.file
        attachments = None

        environment = Environment(
            loader=FileSystemLoader("app/infrastructure/templates")
        )
        template = environment.get_template("newsletter_email.html")
        if file:
            with open(f'app/infrastructure/statics/{file}', mode='rb') as f:
                encoded_file = base64.b64encode(f.read())
            attachments = [
                {
                    "Content-type": "text/plain",
                    "Filename": file,
                    "content": encoded_file.decode()
                }
            ]

        was_ok = True
        for recipient in subscription.recipients:
            unsubscribe_link = f'http://127.0.0.1:8000/newsletter/unsubscription/{recipient.email}'
            html_content = template.render(unsubscribe_link=unsubscribe_link)

            data = {
                'FromEmail': settings.MAILJET_DEFAULT_EMAIL,
                'FromName': "Boletin",
                'Recipients': [
                    {'Email': recipient.email}
                ],
                'Subject': 'test',
                'Html-part': html_content,
                'SandboxMode': False,
                "Attachments": attachments
            }
            response = requests.post(
                settings.MAILJET_API_URL,
                auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY),
                headers={'Accept': 'application/json'},
                json=data
            )
            if response.ok is False:
                was_ok = False
        return was_ok

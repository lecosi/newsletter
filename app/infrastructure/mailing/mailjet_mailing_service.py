import base64

import requests
from jinja2 import Environment, FileSystemLoader

from app.configuration import config
from app.domain.entities import Subscription
from app.domain.mailing_service import MailingService


class MailjetMailingService(MailingService):

    def send(self, subscription: Subscription) -> bool:
        settings = config.get_settings()
        recipients = subscription.recipients
        file = subscription.newsletter.file
        attachments = None

        environment = Environment(
            loader=FileSystemLoader("app/infrastructure/templates")
        )
        template = environment.get_template("newsletter_email.html")
        unsubscribe_link = ''
        html_content = template.render(unsubscribe_link=unsubscribe_link)

        if file:
            filename = file.filename
            encoded_file = base64.b64encode(file)
            attachments = [
                {
                    "Content-type": "text/plain",
                    "Filename": filename,
                    "content": encoded_file
                }
            ]

        data = {
            'FromEmail': settings.MAILJET_DEFAULT_EMAIL,
            'FromName': "Boletin",
            'Recipients': [
                {'Email': recipient.email for recipient in recipients}
            ],
            'Subject': 'test',
            'Html-part': html_content,
            'SandboxMode': True,
            "Attachments": attachments
        }
        response = requests.post(
            settings.MAILJET_API_URL,
            auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY),
            headers={'Accept': 'application/json'},
            json=data
        )
        return response.ok

import uuid

from app.application.use_cases import NewsletterGetListData
from app.domain.entities import Newsletter


def test_newsletter_get_data(newsletter_fixture, newsletter_repository):
    newsletter_id = str(uuid.uuid4())
    newsletter_name = "boletin"

    newsletter_repository.get_all.return_value = [Newsletter(
        id=newsletter_id,
        name=newsletter_name,
        file=None
    )]
    newsletter_creator = NewsletterGetListData(
        newsletter_repository=newsletter_repository
    )

    newsletter = newsletter_creator.get_all()

    assert newsletter[0].id == newsletter_id
    assert newsletter[0].name == newsletter_name

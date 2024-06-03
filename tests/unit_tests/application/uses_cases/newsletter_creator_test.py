from app.application.use_cases import NewsletterCreator


def test_create_newsletter(newsletter_fixture, newsletter_repository):
    newsletter_name = "boletin"

    newsletter_creator = NewsletterCreator(
        newsletter_name=newsletter_name,
        newsletter_repository=newsletter_repository
    )

    newsletter = newsletter_creator.create()

    assert newsletter.id
    assert newsletter.name == newsletter_name

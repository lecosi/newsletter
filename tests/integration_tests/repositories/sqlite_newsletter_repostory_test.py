from app.infrastructure.repositories import SqliteNewsletterRepository


def test_get_by_id_newsletter(create_db, newsletter_fixture):
    repository = SqliteNewsletterRepository()
    repository.add(newsletter_fixture)

    fetched_newsletter = repository.get_by_id(newsletter_fixture.id)

    assert newsletter_fixture.id == fetched_newsletter.id

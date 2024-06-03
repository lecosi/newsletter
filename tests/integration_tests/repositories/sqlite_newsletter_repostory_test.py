from app.infrastructure.repositories import SqliteNewsletterRepository


def test_get_by_id_newsletter(create_db, newsletter_fixture):
    repository = SqliteNewsletterRepository()
    repository.add(newsletter_fixture)

    fetched_newsletter = repository.get_by_id(newsletter_fixture.id)

    assert newsletter_fixture.id == fetched_newsletter.id


def test_get_newsletter_list(create_db, newsletter_fixture):
    repository = SqliteNewsletterRepository()
    repository.add(newsletter_fixture)
    newsletter_list = repository.get_all()
    assert newsletter_list[0].id == newsletter_fixture.id

from unittest.mock import MagicMock

from pytest import fixture

from app.infrastructure.repositories import SqliteSubscriptionRepository, \
    SqliteNewsletterRepository


@fixture
def subscription_repository(mocker):
    subscription_repository = MagicMock()
    mocker.patch.object(
        SqliteSubscriptionRepository,
        '__new__',
        return_value=subscription_repository
    )
    return subscription_repository


@fixture
def newsletter_repository(mocker):
    newsletter_repository = MagicMock()
    mocker.patch.object(
        SqliteNewsletterRepository,
        '__new__',
        return_value=newsletter_repository
    )
    return newsletter_repository

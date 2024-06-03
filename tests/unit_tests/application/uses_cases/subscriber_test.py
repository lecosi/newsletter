from app.application.use_cases import Subscriber


def test_subscribe_one_email_address(subscription_repository,
                                     newsletter_repository,
                                     newsletter_fixture):
    newsletter_repository.get_by_id.return_value = newsletter_fixture
    email_addresses = ("test@gmail.com",)
    subscriber = Subscriber(
        email_addresses=email_addresses,
        newsletter_id=newsletter_fixture.id,
        subscription_repository=subscription_repository,
        newsletter_repository=newsletter_repository
    )

    subscription = subscriber.subscribe()

    subscription_repository.add.assert_called_once_with(subscription)

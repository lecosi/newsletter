from app.application.use_cases.unsubscriber import Unsubscriber


def test_success(mocker, test_client):
    use_case = mocker.patch.object(Unsubscriber, 'unsubscribe')
    email_recipient = 'test@test.com'

    response = test_client.get(
        f'/newsletter/unsubscription/{email_recipient}'
    )

    assert response.status_code == 200
    use_case.assert_called_once()

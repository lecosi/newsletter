from app.application.use_cases.unsubscriber import Unsubscriber


def test_success(mocker, test_client):
    use_case = mocker.patch.object(Unsubscriber, 'unsubscribe')
    email_recipient = 'test@test.com'

    response = test_client.post(
        '/newsletter/unsubscription',
        json={
            'email_recipient': email_recipient
        }
    )

    assert response.status_code == 200
    use_case.assert_called_once()

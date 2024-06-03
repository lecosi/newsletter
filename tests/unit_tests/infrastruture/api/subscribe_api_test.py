from app.application.use_cases import Subscriber


def test_success(mocker, test_client):
    use_case = mocker.patch.object(Subscriber, 'subscribe')
    email_recipients = ['test@test.com']

    response = test_client.post(
        '/newsletter/subscription',
        json={
            'newsletter_id': '1',
            'email_recipients': email_recipients
        }
    )

    assert response.status_code == 200
    use_case.assert_called_once()

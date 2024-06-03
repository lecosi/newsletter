from app.application.use_cases import NewsletterSender


def test_send_newsletter(mocker, test_client):
    use_case = mocker.patch.object(NewsletterSender, 'send')
    use_case.return_value = True

    response = test_client.post(
        '/newsletter/send',
        json={'newsletter_id': '1'}
    )

    data = response.json()

    assert response.status_code == 200
    use_case.assert_called_once()
    assert data['ok'] is True

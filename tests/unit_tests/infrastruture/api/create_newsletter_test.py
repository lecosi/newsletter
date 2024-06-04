import uuid

from app.application.use_cases import NewsletterCreator, Subscriber
from app.domain.entities import Newsletter


def test_success(mocker, test_client):
    use_case_news_letter = mocker.patch.object(NewsletterCreator, 'create')
    mocker.patch.object(Subscriber, 'subscribe')
    newsletter_id = str(uuid.uuid4())
    newsletter_name = "boletin"
    newsletter = Newsletter(id=newsletter_id, name=newsletter_name, file=None)
    use_case_news_letter.return_value = newsletter

    response = test_client.post(
        '/newsletter',
        data={
            'name': newsletter_name,
            'recipients': 'test@test.com,test2@test.com'
        }
    )
    data = response.json()
    assert response.status_code == 201
    assert data['name'] == newsletter_name
    assert data['id'] == newsletter_id
    use_case_news_letter.assert_called_once()

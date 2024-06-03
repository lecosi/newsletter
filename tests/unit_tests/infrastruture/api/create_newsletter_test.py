import uuid

from app.application.use_cases import NewsletterCreator
from app.domain.entities import Newsletter


def test_success(mocker, test_client):
    use_case = mocker.patch.object(NewsletterCreator, 'create')
    newsletter_id = str(uuid.uuid4())
    newsletter_name = "boletin"
    newsletter = Newsletter(id=newsletter_id, name=newsletter_name)
    use_case.return_value = newsletter

    response = test_client.post(
        '/newsletter',
        json={
            'name': newsletter_name
        }
    )
    data = response.json()
    assert response.status_code == 201
    assert data['name'] == newsletter_name
    assert data['id'] == newsletter_id
    use_case.assert_called_once()

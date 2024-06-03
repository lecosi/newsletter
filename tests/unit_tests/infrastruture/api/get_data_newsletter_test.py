import uuid

from app.application.use_cases import NewsletterGetListData
from app.domain.entities import Newsletter


def test_success(mocker, test_client):
    use_case = mocker.patch.object(NewsletterGetListData, 'get_all')
    newsletter_id = str(uuid.uuid4())
    newsletter_name = "boletin"
    newsletter_list = [Newsletter(id=newsletter_id, name=newsletter_name)]
    use_case.return_value = newsletter_list

    response = test_client.get('/newsletter')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['_name'] == newsletter_name
    assert data[0]['_id'] == newsletter_id
    use_case.assert_called_once()

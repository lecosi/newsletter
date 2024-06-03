import uuid

from pytest import fixture

from app.domain.entities import Newsletter


@fixture
def newsletter_fixture():
    return Newsletter(name="test", id=str(uuid.uuid4()))

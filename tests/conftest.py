import uuid

from pytest import fixture
from starlette.testclient import TestClient

from app.domain.entities import Newsletter
from main import app


@fixture
def newsletter_fixture():
    return Newsletter(name="test", id=str(uuid.uuid4()), file=None)


@fixture
def test_client():
    return TestClient(app)

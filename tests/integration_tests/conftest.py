import os
import sqlite3
from pathlib import Path

from pytest import fixture

from app.configuration import config


@fixture(scope='session')
def settings():
    os.environ['APP_ENVIRONMENT'] = 'test'
    return config.get_settings()


@fixture
def create_db(settings):
    path = settings.DATABASE_URL
    path.unlink(missing_ok=True)
    connection = sqlite3.connect(str(path))
    schema_path = Path(settings.ROOT_PATH / 'tests' / 'integration_tests' / 'db_schema.sql')
    with open(schema_path) as schema:
        connection.executescript(schema.read())

    yield
    path.unlink()

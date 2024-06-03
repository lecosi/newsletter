import os
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    ROOT_PATH: Path = Path(__file__).parent.parent.parent
    DATABASE_URL = ROOT_PATH / 'db.sql'
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    MAILJET_API_URL: str = os.getenv("MAILJET_API_URL")
    MAILJET_API_KEY: str = os.getenv("MAILJET_API_KEY")
    MAILJET_SECRET_KEY: str = os.getenv("MAILJET_SECRET_KEY")
    MAILJET_DEFAULT_EMAIL: str = os.getenv("MAILJET_DEFAULT_EMAIL")
    ALGORITHM = "HS256"

    class Config:
        case_sensitive = True


class TestSettings(Settings):
    DATABASE_URL = Settings.ROOT_PATH / 'db.sql'


def get_settings() -> Settings:
    env = os.getenv('APP_ENVIRONMENT')
    if env == 'test':
        return TestSettings()
    return Settings()

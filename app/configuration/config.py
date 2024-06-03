import os
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    ROOT_PATH: Path = Path(__file__).parent.parent.parent
    USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "newsletter_db")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                   f"@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
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


def get_database_uri() -> str:  # pragma: no cover
    #if settings.USE_SQLITE_DB:
    #    return "sqlite:///./sql_app.db"
    return Settings.DATABASE_URL

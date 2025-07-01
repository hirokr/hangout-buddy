from pydantic import EmailStr, Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os
# Load .env file explicitly
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Settings(BaseSettings):
    # App Config
    PROJECT_NAME: str = "Hangout Buddy"
    API_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = "development"

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    ALGORITHM: str = "HS256"

    # Database
    DATABASE_URL: str

    # OAuth
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""

    FACEBOOK_CLIENT_ID: str = ""
    FACEBOOK_CLIENT_SECRET: str = ""

    TWITTER_CLIENT_ID: str = ""
    TWITTER_CLIENT_SECRET: str = ""

    # Email
    SENDGRID_API_KEY: str = ""
    EMAIL_FROM: EmailStr = "no-reply@hangoutbuddy.com"

    # SQL
    SQLALCHEMY_ECHO: bool = True

    # 🟢 This line tells Pydantic to ignore unknown variables like redis_url
    model_config = {
        "extra": "ignore",
        "env_file": BASE_DIR / ".env",
        "env_prefix": "",
    }


settings = Settings() # type: ignore

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from app import ROOT_DIR


class ImagesSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(ROOT_DIR).parent / ".env", extra="ignore")


class Settings(ImagesSettings):
    unsplash_access_key: str = Field(
        validation_alias="UNSPLASH_ACCESS_KEY", default="default-access-key"
    )
    unsplash_base_url: str = Field(validation_alias="UNSPLASH_BASE_URL", default="base-url")
    database_url: str = Field(validation_alias="DATABASE_URL", default="db_url")
    debug: int = 1


settings = Settings()

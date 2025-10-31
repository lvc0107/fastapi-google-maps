from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from images_project import ROOT_DIR


class ImagesSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(ROOT_DIR).parent / ".env", extra="ignore")


class Settings(ImagesSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/mapsdb"
    prefix_path: str = ""
    debug: int = 1


settings = Settings()

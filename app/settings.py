import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/mapsdb"

    class Config:
        env_file = ".env"

settings = Settings()

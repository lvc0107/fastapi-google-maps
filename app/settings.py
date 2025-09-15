
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/mapsdb"
    prefix_path: str = ""
    debug: int =  1
    class Config:
        env_file = ".env"

settings = Settings()

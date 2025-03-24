from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow", env_file=".env")

    DATABASE_URL: str


settings = Settings()
from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Settings for the research agent.
    """

    DATABASE_URL: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
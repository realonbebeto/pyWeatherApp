from pydantic import BaseSettings


class Settings(BaseSettings):
    geo_access_token: str
    meteo_access_token: str

    class Config:
        env_file = "app/.env"


settings = Settings()

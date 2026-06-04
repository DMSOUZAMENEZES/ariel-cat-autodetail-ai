from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://autodetail:autodetail@postgres:5432/autodetail"
    redis_url: str = "redis://redis:6379/0"
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

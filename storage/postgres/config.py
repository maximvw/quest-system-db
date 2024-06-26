from pydantic_settings import BaseSettings

class PgConfig(BaseSettings):
    port: str = "5432"
    user: str = "postgres"
    password: str = "1234"
    db_name: str = "stalker-quests"
from pydantic_settings import BaseSettings


class PgConfig(BaseSettings):
    port: str = "5432"
    user: str = "postgres"
    password: str = "1234"
    db_name: str = "stalker-quests"

    def get_url(self):
        return f"postgresql://{self.user}:{self.password}@localhost:{self.port}/{self.db_name}"


pg_config = PgConfig()

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class Quest(BaseModel):
    employer: str
    title: str
    description: str
    award: float


class QuestId(BaseModel):
    quest_id: int


class ChangesForQuest(BaseModel):
    employer: str
    description: str
    award: float


class PgConfig(BaseSettings):
    port: str = "5432"
    user: str = "postgres"
    password: str = "1234"
    db_name: str = "stalker-quests"

from pydantic import BaseModel


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

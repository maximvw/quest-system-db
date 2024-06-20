from pydantic import BaseModel


class Quest(BaseModel):
    employer: str
    title: str
    description: str
    award: float

    class Config:
        orm_model = True

class QuestIdsList(BaseModel):
    quest_ids: list


class ChangesForQuest(BaseModel):
    employer: str
    description: str
    award: float

    class Config:
        orm_model = True

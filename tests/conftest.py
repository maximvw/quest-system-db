from unittest.mock import MagicMock, create_autospec

import pytest

import storage.postgres.crud
from server import schemas
from server.main import app
from server.routers.quests import get_db

mock_session = MagicMock()

PUBLISHED_ID = 1


def override_get_db():
    try:
        yield mock_session
    finally:
        pass


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def mock_db_session():
    return mock_session


storage.postgres.crud.get_quest_by_title = create_autospec(
    storage.postgres.crud.get_quest_by_title,
    side_effect=[
        schemas.Quest(title="Find artifact", employer="Boroda", description="AAA", award=600),
        KeyError("Destroy mutants - quest does not exist")
    ]
)

storage.postgres.crud.publish_quest = create_autospec(
    storage.postgres.crud.publish_quest,
    side_effect=[schemas.QuestId(quest_id=PUBLISHED_ID),
                 KeyError(
                     "Ключ title=string уже существует."
                 )]
)

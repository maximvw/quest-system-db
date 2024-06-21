from http import HTTPStatus

from fastapi.testclient import TestClient

from server.main import app
from tests.conftest import PUBLISHED_ID

client = TestClient(app)


def test_show_quests_by_title(mock_db_session):
    title = "Find artifact"
    employer = "Boroda"
    description = "AAA"
    award = 600

    response = client.get(
        f"/quests/show_by_title/{title}"
    )

    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data["employer"] == employer
    assert data["title"] == title
    assert data["description"] == description
    assert data["award"] == award


def test_show_quests_by_title_exception(mock_db_session):
    title = "Kill mutants"

    response = client.get(
        f"/quests/show_by_title/{title}"
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json()['detail'] == "Destroy mutants - quest does not exist"


def test_publish_quest(mock_db_session):
    employer = "Sidorovych"
    title = "Destroy mutants"
    description = "AAA+"
    award = 50

    response = client.post(
        "/quests/publish_quest", json={
            "employer": employer,
            "title": title,
            "description": description,
            "award": award
        }
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['quest_id'] == PUBLISHED_ID


def test_publish_quest_exception(mock_db_session):
    employer = "Sidorovych"
    title = "string"
    description = "AAA+"
    award = 50

    response = client.post(
        "/quests/publish_quest", json={
            "employer": employer,
            "title": title,
            "description": description,
            "award": award
        }
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json()['detail'] == "Ключ title=string уже существует."

from http import HTTPStatus

from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_show_quests_by_title(mock_db_session):
    title = "Find artifact"

    response = client.get(
        f"/quests/show_by_title/{title}"
    )

    assert response.status_code == HTTPStatus.OK


def test_show_quests_by_title_exception(mock_db_session):
    title = "Kill mutants"

    response = client.get(
        f"/quests/show_by_title/{title}"
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST


from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_show_quests_by_employer(mock_db_session):
    employer = "Boroda"

    response = client.get(
        f"/quests//quests/show_by_employer/{employer}"
    )

    assert response.status_code == 200
    data = response.json()



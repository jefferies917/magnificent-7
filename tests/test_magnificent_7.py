from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_magnificent_7():
    response = client.get("/magnificent-7")
    assert response.status_code == 200
    assert "goalkeeper" in response.json()


def test_team_magnificent_7():
    response = client.get("/magnificent-7/team/1")
    assert response.status_code == 200
    assert "goalkeeper" in response.json()

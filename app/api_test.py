from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_count():
    response = client.get("/count")
    assert response.status_code == 200
    assert response.json() == {"count": 11}

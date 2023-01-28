from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_count():
    response = client.get("/count")
    assert response.status_code == 200
    assert response.json() == {"count": 11}


def test_max():
    response = client.get("/max")
    assert response.status_code == 200
    assert response.json() == {"max": 82.0}


def test_mean():
    response = client.get("/mean")
    assert response.status_code == 200
    assert response.json() == {"mean": 28.09}


def test_empty_count_with_from_timestamp():
    response = client.get("/count?from_timestamp=1674811012")
    assert response.status_code == 200
    assert response.json() == {"count": 0}


def test_count_with_from_timestamp():
    response = client.get("/count?from_timestamp=1674306330")
    assert response.status_code == 200
    assert response.json() == {"count": 8}


def test_max_with_to_timestamp():
    response = client.get("/max?to_timestamp=1574749567")
    assert response.status_code == 200
    assert response.json() == {"max": 82}


def test_mean_with_from_to_timestamp():
    response = client.get(
        "/mean?from_timestamp=1274749567&to_timestamp=1524739567")
    assert response.status_code == 200
    assert response.json() == {"mean": 22.7}


def test_zero_mean_with_from_timestamp():
    response = client.get("/mean?from_timestamp=1674895969")
    assert response.status_code == 200
    assert response.json() == {"mean": 0}

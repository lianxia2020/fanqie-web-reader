import pytest
from fastapi.testclient import TestClient

from server import app


@pytest.fixture
def client():
    # Endpoint tests do not need the app's long-running static-file watcher.
    test_client = TestClient(app)
    yield test_client
    test_client.close()


def test_health(client):
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert 'id="app"' in response.text

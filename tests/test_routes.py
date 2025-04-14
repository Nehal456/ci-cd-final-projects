# tests/test_routes.py
import pytest
from service.common import status  # HTTP Status Codes
from service import app  # Import the Flask app instance from __init__.py
from service.common.utils import reset_counters  # Import reset_counters


@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    reset_counters()  # Reset counters before each test
    app.testing = True  # Enable testing mode
    return app.test_client()


def test_index(client):
    """It should call the index endpoint."""
    resp = client.get("/")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.get_json() == {"message": "Welcome to the Counter API"}


def test_health(client):
    """It should be healthy."""
    resp = client.get("/health")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.get_json() == {"status": "OK"}


def test_create_counters(client):
    """It should create a counter."""
    name = "foo"
    resp = client.post(f"/counters/{name}")
    assert resp.status_code == status.HTTP_201_CREATED
    data = resp.get_json()
    assert data["name"] == name
    assert data["counter"] == 0


def test_list_counters(client):
    """It should list all counters."""
    client.post("/counters/foo")  # Create a counter
    resp = client.get("/counters")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.get_json()
    assert len(data) == 1
    assert "foo" in data


def test_read_counter(client):
    """It should read a specific counter."""
    name = "foo"
    client.post(f"/counters/{name}")  # Create a counter
    resp = client.get(f"/counters/{name}")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.get_json()
    assert data["name"] == name
    assert data["counter"] == 0


def test_update_counter(client):
    """It should update (increment) a specific counter."""
    name = "foo"
    client.post(f"/counters/{name}")  # Create a counter
    resp = client.put(f"/counters/{name}")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.get_json()
    assert data["name"] == name
    assert data["counter"] == 1


def test_delete_counter(client):
    """It should delete a counter."""
    name = "foo"
    client.post(f"/counters/{name}")  # Create a counter
    resp = client.delete(f"/counters/{name}")
    assert resp.status_code == status.HTTP_204_NO_CONTENT
    resp = client.get(f"/counters/{name}")
    assert resp.status_code == status.HTTP_404_NOT_FOUND
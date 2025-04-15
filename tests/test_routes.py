import pytest
from service.common.status import HTTPStatus  # Updated import
from service import app
from service.common.utils import reset_counters


@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    reset_counters()
    app.testing = True
    return app.test_client()


def test_index(client):
    """It should call the index endpoint."""
    resp = client.get("/")
    assert resp.status_code == HTTPStatus.OK  # Updated
    assert resp.get_json() == {"message": "Welcome to the Counter API"}


def test_health(client):
    """It should be healthy."""
    resp = client.get("/health")
    assert resp.status_code == HTTPStatus.OK  # Updated
    assert resp.get_json() == {"status": "OK"}


def test_create_counters(client):
    """It should create a counter."""
    name = "foo"
    resp = client.post(f"/counters/{name}")
    assert resp.status_code == HTTPStatus.CREATED  # Updated
    data = resp.get_json()
    assert data["name"] == name
    assert data["counter"] == 0


def test_list_counters(client):
    """It should list all counters."""
    client.post("/counters/foo")
    resp = client.get("/counters")
    assert resp.status_code == HTTPStatus.OK  # Updated
    data = resp.get_json()
    assert len(data) == 1
    assert "foo" in data


def test_read_counter(client):
    """It should read a specific counter."""
    name = "foo"
    client.post(f"/counters/{name}")
    resp = client.get(f"/counters/{name}")
    assert resp.status_code == HTTPStatus.OK  # Updated
    data = resp.get_json()
    assert data["name"] == name
    assert data["counter"] == 0


def test_update_counter(client):
    """It should update (increment) a specific counter."""
    name = "foo"
    client.post(f"/counters/{name}")
    resp = client.put(f"/counters/{name}")
    assert resp.status_code == HTTPStatus.OK  # Updated
    data = resp.get_json()
    assert data["name"] == name
    assert data["counter"] == 1


def test_delete_counter(client):
    """It should delete a

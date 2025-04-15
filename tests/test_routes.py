import pytest
from service.common.status import HTTPStatus
from service import create_app  # Changed from direct app import
from service.common.utils import reset_counters


@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    app = create_app()  # Create fresh app instance
    reset_counters()
    app.testing = True
    
    # Clear counters before each test
    from service.routes import counters
    counters.clear()
    
    return app.test_client()


def test_index(client):
    """Test the index endpoint."""
    resp = client.get("/")
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"message": "Welcome to the Counter API"}


def test_health(client):
    """Test health check endpoint."""
    resp = client.get("/health")
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"status": "OK"}


def test_create_counters(client):
    """Test counter creation."""
    name = "test-counter"
    resp = client.post(f"/counters/{name}")
    assert resp.status_code == HTTPStatus.CREATED
    data = resp.get_json()
    assert data["name"] == name
    assert data["counter"] == 0


def test_list_counters(client):
    """Test listing all counters."""
    client.post("/counters/test-counter")
    resp = client.get("/counters")
    assert resp.status_code == HTTPStatus.OK
    data = resp.get_json()
    assert isinstance(data, dict)
    assert "test-counter" in data


def test_read_counter(client):
    """Test reading specific counter."""
    name = "test-counter"
    client.post(f"/counters/{name}")
    resp = client.get(f"/counters/{name}")
    assert resp.status_code == HTTPStatus.OK
    data = resp.get_json()
    assert data["name"] == name
    assert data["counter"] == 0


def test_update_counter(client):
    """Test incrementing a counter."""
    name = "test-counter"
    client.post(f"/counters/{name}")
    resp = client.put(f"/counters/{name}")
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json()["counter"] == 1


def test_delete_counter(client):
    """Test counter deletion."""
    name = "test-counter"
    client.post(f"/counters/{name}")
    resp = client.delete(f"/counters/{name}")
    assert resp.status_code == HTTPStatus.NO_CONTENT
    resp = client.get(f"/counters/{name}")
    assert resp.status_code == HTTPStatus.NOT_FOUND

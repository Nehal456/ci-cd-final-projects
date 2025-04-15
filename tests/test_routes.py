import pytest
from service.common.status import HTTPStatus
from service import create_app
from service.routes import counters  # Import counters directly
from service.common.utils import reset_counters

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    app = create_app()
    reset_counters()
    app.testing = True
    counters.clear()  # Clear counters before each test
    return app.test_client()

def test_index(client):
    """Test the index endpoint."""
    resp = client.get("/api/")
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"message": "Welcome to the Counter API"}

def test_health(client):
    """Test health check endpoint."""
    resp = client.get("/api/health")
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"status": "OK"}

def test_create_counters(client):
    """Test counter creation."""
    resp = client.post("/api/counters/test-counter")
    assert resp.status_code == HTTPStatus.CREATED
    assert resp.get_json() == {"name": "test-counter", "counter": 0}
    assert "test-counter" in counters

def test_list_counters(client):
    """Test listing counters."""
    client.post("/api/counters/test-counter")
    resp = client.get("/api/counters")
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"test-counter": 0}

def test_read_counter(client):
    """Test reading a counter."""
    client.post("/api/counters/test-counter")
    resp = client.get("/api/counters/test-counter")
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"name": "test-counter", "counter": 0}

def test_update_counter(client):
    """Test updating a counter."""
    client.post("/api/counters/test-counter")
    resp = client.put("/api/counters/test-counter")
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"name": "test-counter", "counter": 1}

def test_delete_counter(client):
    """Test deleting a counter."""
    client.post("/api/counters/test-counter")
    resp = client.delete("/api/counters/test-counter")
    assert resp.status_code == HTTPStatus.NO_CONTENT
    resp = client.get("/api/counters/test-counter")
    assert resp.status_code == HTTPStatus.NOT_FOUND

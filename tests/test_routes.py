import pytest
from service.common.status import HTTPStatus
from service import create_app  # Import the factory function
from service.common.utils import reset_counters

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    app = create_app()  # Create new app instance
    reset_counters()
    app.testing = True
    
    # Clear counters before each test
    from service.routes import counters
    counters.clear()
    
    return app.test_client()

def test_index(client):
    """Test the index endpoint."""
    resp = client.get("/api/")  # Note the /api prefix
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"message": "Welcome to the Counter API"}

def test_health(client):
    """Test health check endpoint."""
    resp = client.get("/api/health")  # Note the /api prefix
    assert resp.status_code == HTTPStatus.OK
    assert resp.get_json() == {"status": "OK"}

# Update all other test routes to include /api prefix
def test_create_counters(client):
    resp = client.post("/api/counters/foo")  # Note /api prefix
    assert resp.status_code == HTTPStatus.CREATED

# ... continue with other tests, all using /api prefix ...

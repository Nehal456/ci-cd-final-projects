"""This module initializes the Flask application."""
# service/routes.py
from service import app
from service.common.utils import COUNTERS


@app.route("/", methods=["GET"])
def index():
    """Root endpoint."""
    return {"message": "Welcome to the Counter API"}, 200


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return {"status": "OK"}, 200


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Create a new counter."""
    if name in COUNTERS:
        return {"error": "Counter already exists"}, 409
    COUNTERS[name] = 0
    return {"name": name, "counter": COUNTERS[name]}, 201


@app.route("/counters", methods=["GET"])
def list_counters():
    """List all counters."""
    return COUNTERS, 200


@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a specific counter."""
    if name not in COUNTERS:
        return {"error": "Counter not found"}, 404
    return {"name": name, "counter": COUNTERS[name]}, 200


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Update (increment) a specific counter."""
    if name not in COUNTERS:
        return {"error": "Counter not found"}, 404
    COUNTERS[name] += 1
    return {"name": name, "counter": COUNTERS[name]}, 200


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a specific counter."""
    if name in COUNTERS:
        del COUNTERS[name]
    return "", 204

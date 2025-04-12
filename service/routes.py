from service import app  # Import the app object from __init__.py
from flask import jsonify


@app.route('/some-endpoint', methods=['GET'])
def some_endpoint():
    return jsonify({
        "message": "Success"
    }), 200


@app.route('/error-endpoint', methods=['GET'])
def error_endpoint():
    return jsonify({
        "error": "Invalid request, missing required fields."
    }), 400

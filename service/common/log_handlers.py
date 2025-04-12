from flask import jsonify
from service import app  # Import the Flask app


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

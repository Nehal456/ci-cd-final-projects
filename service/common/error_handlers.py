from flask import jsonify


def handle_error(error, error_code):
    return jsonify(
        status=error_code,
        error=str(error)
    ), error_code

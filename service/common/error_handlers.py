"""
Error handlers for the service
Provides consistent error responses across the service
"""

from flask import jsonify
from service import app
from http import HTTPStatus


@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found(error):
    """Handle 404 Not Found errors"""
    return (
        jsonify(
            status=HTTPStatus.NOT_FOUND,
            error="Not Found",
            message=str(error)
        ),
        HTTPStatus.NOT_FOUND
    )


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    """Handle 500 Internal Server errors"""
    return (
        jsonify(
            status=HTTPStatus.INTERNAL_SERVER_ERROR,
            error="Internal Server Error",
            message=str(error)
        ),
        HTTPStatus.INTERNAL_SERVER_ERROR
    )


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    """Handle all unexpected exceptions"""
    status_code = getattr(error, "code", HTTPStatus.INTERNAL_SERVER_ERROR)
    if not isinstance(status_code, int) or status_code < 100 or status_code >= 600:
        status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    
    return (
        jsonify(
            status=status_code,
            error=error.__class__.__name__,
            message=str(error)
        ),
        status_code
    )
"""
HTTP Status codes
Provides common HTTP status codes for the service
"""


class HTTPStatus:
    """Enumeration of HTTP status codes"""
    # 2xx Success
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    
    # 4xx Client Errors
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    
    # 5xx Server Errors
    INTERNAL_SERVER_ERROR = 500

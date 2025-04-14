# service/__init__.py
from flask import Flask
from service.common.log_handlers import init_logging

# Create the Flask app instance
app = Flask(__name__)

# Initialize logging
init_logging(app, "gunicorn.error")

# Import routes to register them
import service.routes  # Ensure routes are registered
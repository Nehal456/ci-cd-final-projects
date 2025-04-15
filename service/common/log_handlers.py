"""
Log handling utilities
Provides consistent logging across the service
"""
import logging  # ADD THIS IMPORT AT THE TOP

def init_logging(app):
    """Initialize logging"""
    if app.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    # Add other logging configuration as needed
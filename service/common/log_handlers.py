# service/common/log_handlers.py
import logging

def init_logging(app, logger_name):
    """Initialize logging for the application."""
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    app.logger.handlers = logger.handlers
    app.logger.setLevel(logger.level)
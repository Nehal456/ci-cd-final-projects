"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# Imports must happen after Flask app creation
# pylint: disable=wrong-import-position
from service import routes  # noqa: E402
from service.common import log_handlers  # noqa: E402
# pylint: enable=wrong-import-position

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

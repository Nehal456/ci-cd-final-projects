from flask import Flask
from service.routes import bp as routes_bp

# Initialize the Flask application
app = Flask(__name__)

# Register the blueprint with the Flask app
app.register_blueprint(routes_bp, url_prefix="/api")

# Any other setup can follow here

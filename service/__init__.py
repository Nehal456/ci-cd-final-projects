from flask import Flask

def create_app():
    """Factory function to create and configure the Flask app"""
    app = Flask(__name__)
    
    # Import and register blueprints
    from service.routes import bp as routes_bp
    app.register_blueprint(routes_bp, url_prefix="/api")
    
    return app

# Create app instance
app = create_app()

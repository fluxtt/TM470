from flask import Flask
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # In production, use a secure method to set this key
    
    app.register_blueprint(auth_bp)
    
    @app.route("/")
    def home():
        return "Welcome to the Inventory Management System!"
    
    return app
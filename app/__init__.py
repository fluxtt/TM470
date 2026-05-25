from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return "Welcome to the Inventory Management System!"
    
    # from app.routes.inventory_routes import inventory_bp
    # app.register_blueprint(inventory_bp)
    
    return app
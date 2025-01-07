from flask import Flask
# from _infrastructure.adapters.output.router_view_file_adapter import db
from _infrastructure.adapters.output.database.object import db
from _infrastructure.config.appConfig import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Configure your SQLite database (or any other DB you want)

    db.init_app(app)

    # Create the tables (for demo purposes, we do it on startup)
    with app.app_context():
        from driver.routes_controller import Routes
        Routes(app)
        
        db.create_all()
    
    return app

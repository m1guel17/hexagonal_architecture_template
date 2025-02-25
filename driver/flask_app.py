from flask import Flask
from _infrastructure.adapters.output.database.object import db
from _infrastructure.config.appConfig import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from _infrastructure.adapters.input import RoutersAPI
        RoutersAPI(app)
        
        db.create_all()
    
    return app

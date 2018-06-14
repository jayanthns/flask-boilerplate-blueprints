from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app(config_name, register_blueprint=True):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    if register_blueprint:
        from apps.users.views import users_blueprint
        app.register_blueprint(users_blueprint, url_prefix='/users')

        from apps.users.api.views import users_api_blueprint
        app.register_blueprint(users_api_blueprint, url_prefix='/api/users')

    return app

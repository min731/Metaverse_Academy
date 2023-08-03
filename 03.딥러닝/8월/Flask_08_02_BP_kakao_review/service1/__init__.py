from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

from . import models

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app,db)

    from .views import main_views,task1_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(task1_views.bp)

    return app
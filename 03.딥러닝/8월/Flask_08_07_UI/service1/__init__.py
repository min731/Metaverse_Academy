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

    from .views import main_views,task1_views,task2_views,question_views,answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(task1_views.bp)
    app.register_blueprint(task2_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app

# model.pt 다운 후
# pytorch.org
# 일단 CPU 버전으로 설치
# pip3 install torch torchvision torchaudio


# 부트스트랩 다운로드 - https://getbootstrap.com/docs/5.1/getting-started/download/
# 다운 후 압축 해제
# css-bootstrap.min (css파일) 사용


# 모든 form은 이것으로 사용
# pip install flask-wtf
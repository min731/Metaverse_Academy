from flask import Flask

# Flask로 DB를 다룰 때, flask_migrate, flask_sqlalchemy 필요
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

from . import models

def create_app():
    app = Flask(__name__)

    # config 파일의 설정값들이 flask에 등록
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app,db)

    from .views import kakao_views,dl_views
    app.register_blueprint(kakao_views.bp)
    app.register_blueprint(dl_views.bp)

    return app

# Flask에서 DB 연동할 때 
# flask db init

# DB에 새로운 테이블을 만들거나 수정할 때, class 테이블 만든 후
# flask db migrate

# flask db upgrade

# 생성된 db 파일 확인을 위해
# https://sqlitebrowser.org/dl/ 
# DB Browser for SQLite - Standard installer for 64-bit Windows 설치
# models.py로 만든 테이블 생성되어 있음, 또 alembic_version 테이블 생성되어 있음 (migrations-version-aa40c8894f1d_.py 생성되어있음)

# 1. 가상환경 설정
# 2. FLASK 프로젝트 생성
# 3. 블루프린트 설정
# 4. 데이터베이스 설정
# 5. 테이블 생성
# 6. 테이블에 데이터 업로드
from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAL

def create_app():
    app = Flask(__name__)

    from .views import main_views,classification_views,chat_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(classification_views.bp)
    app.register_blueprint(chat_views.bp)

    return app

# set FLASP_APP=app
# flask run

# Blueprint : 라우터를 관리해줌

# 서버 실행 중 코드 수정 가능 
# set FLASK_DEBUG=True
# 'Debug Mode : on'

# postman 설치 (Client 서버 구동 확인)
# https://www.postman.com/downloads/
# 키값 받아야함
# collections - New Request - 주소입력해서 확인

# ORM (파이썬 기반 쿼리문)
# ORM을 쓰게되면 데이터베이스에 관계없이 코드를 유지할 수 있다.
# pip flask-migrate
# 보통 모델 서버, DB서버 따로따로 만듬
# *환경 설정 app폴더와 '같은 경로'에 config.py 파일 만듬
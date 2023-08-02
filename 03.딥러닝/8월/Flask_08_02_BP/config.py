import os

# 설치없이 사용할 수 있는 DB 사용 : SQLite
# MYSQL로 하고 싶을 시, Flask SQLAlchemy Mysql 검색

BASE_DIR = os.path.dirname(__file__) # 현재 디렉토리 이름 가져옴

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'app.db')) # app.db에 접근해라
SQLALCHEMY_TRACK_MODIFICATIONS = False
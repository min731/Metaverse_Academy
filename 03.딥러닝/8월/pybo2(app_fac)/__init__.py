# 플라스크 구조
# https://wikidocs.net/81044

# 데이터베이스를 처리하는 model
# 서버로 전송된 폼을 처리한느 forms
# views 안에는 도메인을 쪼개 놓음
# statics는 디자인
# templates hmtl 파일 저장
# config는 암호 저장

# 순환 참조 오류
# 자기 자신을 참조하는 오류
# import 불가 오류가 뜰 수 있음
# application factory 방식을 사용
#https://wikidocs.net/81504
from flask import Flask

# 함수를 통해 app을 생성하면 순환 참조 오류가 생기지 않음
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app

# set FLASK_APP=pybo
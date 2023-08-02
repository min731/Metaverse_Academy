# 1)
# chatbot앱 => (text 전달) => 추론 서버
#           <= (추론 결과) <=

# 2)
# chatbot앱 => (text 전달) => 서비스 서버 => (text 전달) => 추론 서버
#           <= (추론 결과) <=            <= (추론 결과) <=
# * 서비스 서버에서 채팅 데이터를 축적해놓아야만 나중에 재학습시킬때 활용할 수 있음

# http : // 주소 : 포트번호
#                 (주로 8080포트)


# https://wikidocs.net/book/4542
# pip install --upgrade pip

# 데이터가 전달되면 flask가 감지함
from flask import Flask

# __name__ 실행하고 있는 파일의 이름
app = Flask(__name__)

# route
# http://127.0.0.1:5000/

# 실행
# flask 프로젝트 새로 파는 것이 좋음
# set FLASK_APP=pybot(flask)
# export FLASK_APP=pybot(flask)
# flask run

@app.route('/')
def hello_pybot():
    return 'Hello, Pybo!'

@app.route('/chatbot')
def chatbot():
    return '안녕, 나는 챗봇'

# flask 껐는데 port가 사용중이다 라고 나오면
# 컴퓨터 껐다키면 됌

# 플라스크 기본 구조
# https://wikidocs.net/81044
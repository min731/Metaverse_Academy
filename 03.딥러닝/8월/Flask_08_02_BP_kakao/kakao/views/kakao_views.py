from flask import Blueprint

# 요청으로 받을 때
from flask import request

bp = Blueprint('main',__name__,url_prefix='/kakao')

# ex) request 받기
# postman - body - key:chat, value:Hi

@bp.route('/chat')
def kakao_chat():
    result = request.form
    print(result)
    print(result['chat'])
    return '(bp) kakao_chat \n 안녕하세요 카카오입니다.'

@bp.route('/ml')
def kakao_ml():
    return '(bp) kakao_ml \n 머신러닝입니다.'



# 데이터베이스에 입력받을 때
from kakao.models import Question,Answer
from datetime import datetime
from kakao import db

@bp.route('/qna')
def kakao_qna():

    # Qusetion 테이블의 subject 컬럼
    q = Question(subject='질문1',content='고양이 맞나요?',create_date = datetime.now())
    
    # session에 한꺼번에 모아서 처리
    db.session.add(q)

    # 저장된 내역 실제 db에 upgrade
    db.session.commit()

    return '(bp) kakao_qna \n db.session 커밋'
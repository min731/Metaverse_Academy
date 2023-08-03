from flask import Blueprint
from flask import request

bp = Blueprint('task1',__name__,url_prefix='/task1')

@bp.route('/catdog')
def task1_whats():
    result = request.form
    print(result)
    print(result['image'])
    return 'BP cat or dog'

@bp.route('/gender')
def task1_gender():
    return 'BP F or M'

from service1.models import Question,Answer
from datetime import datetime
from service1 import db

@bp.route('/qna')
def kakao_qna():

    # Qusetion 테이블의 subject 컬럼
    q = Question(subject='질문1',content='고양이 맞나요?',create_date = datetime.now())
    
    # session에 한꺼번에 모아서 처리
    db.session.add(q)

    # 저장된 내역 실제 db에 upgrade
    db.session.commit()

    return '(bp) kakao_qna \n db.session 커밋'
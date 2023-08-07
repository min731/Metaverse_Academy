from flask import Blueprint
from flask import request

bp = Blueprint('task1',__name__,url_prefix='/task1')

@bp.route('/catdog')
def task1_whats():
    result = request.form
    print(result)
    # print(result['image'])
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

# Flask ORM 문법 검색
# DB에서 데이터 가져오기
@bp.route('/get_question')
def get_question():
    # questions = Question.query.all() # [q1,q2...]
    # print("체크 questions : ",questions)
    # print("체크 len(questions) : ",len(questions))
    # print("체크 questions[0].id : ",questions[0].id)
    # print("체크 questions[0].subject : ",questions[0].subject)

    # *** 찾고자하는 question만 가져오기

    # id == 1
    # result = Question.query.filter(Question.id==1).all()
    # print("체크 questions : ",result)
    # print("체크 len(questions) : ",len(result))
    # print("체크 questions[0].id : ",result[0].id)
    # print("체크 questions[0].subject : ",result[0].subject)
    # print("체크 questions[0].content : ",result[0].content)

    # like
    # result = Question.query.filter(Question.content.like('%고양이%')).all()
    # print("체크 questions : ",result)
    # print("체크 len(questions) : ",len(result))
    # print("체크 questions[0].id : ",result[0].id)
    # print("체크 questions[0].subject : ",result[0].subject)
    # print("체크 questions[0].content : ",result[0].content)

    # *** DB 데이터 수정하기

    # get() : pk값으로 참조
    # result = Question.query.get(1)
    # result.subject = '질문1(수정)' # 수정
    # db.session.commit() # 저장

    # *** DB 데이터 삭제하기
    result = Question.query.get(1)
    db.session.delete(result)
    db.session.commit()

    return 'DB 조작 성공'
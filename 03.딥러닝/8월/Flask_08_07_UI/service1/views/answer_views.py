from flask import Blueprint, url_for, request
# redirect 기능
from werkzeug.utils import redirect

from datetime import datetime

# 입력된 데이터 저장하기 위함
from service1 import db

from service1.models import Question,Answer

bp = Blueprint('answer',__name__,url_prefix='/answer')


@bp.route('/create/<int:q_id>',methods=['POST'])
def create(q_id):
    # Question 테이블에서 q_id에 해당하는 질문을 가져옴
    # 테이블에 없는 키라면 404 표시하게함
    question = Question.query.get_or_404(q_id)
    content = request.form['content']

    answer = Answer(content=content,create_date=datetime.now())

    # 입련된 답변을 질문에 저장함
    question.answer_set.append(answer)
    db.session.commit()

    return redirect(url_for('question.detail',q_id = q_id))
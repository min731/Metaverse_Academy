from flask import Blueprint

# web을 위한 패키지
from flask import render_template # html
from service1.models import Question

# form 패키지
from pybo.forms import QuestionForm

bp = Blueprint('question',__name__,url_prefix='/question')

@bp.route('/list')
def q_list():
    # create_date column기준으로 정렬해서 가져오기
    q_list = Question.query.order_by(Question.create_date.desc())

    print(q_list)
    # Jinja2 덕분에 html에 변수 선언,조건문을 통해 작성할 수 있음
    return render_template('q_list/q_list.html',q_list=q_list)

    # 이후 템플릿을 만들어줌
    # service1/templates에 만들기
    # service1/templates/q_list/q_list.html 만들기
    # html 파일에 jinja2 문법으로 작성

# q_list.html에서 링크누르면 이동
@bp.route('/detail/<int:q_id>/')
def detail(q_id):
    print("체크 q_id :",q_id)
    
    # 페이지가 없을 시 404 오류 뜨게함 
    question = Question.query.get_or_404(q_id)  
    # question = Question.query.get(q_id)
    return render_template('q_list/q_detail.html',question=question)

# 질문 등록하는 
@bp.route('/create/')
def create():
    form = QuestionForm()
    return render_template('question/question_form.html', form=form)
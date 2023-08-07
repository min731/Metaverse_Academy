from flask import Blueprint

# web을 위한 패키지
from flask import render_template # html
from service1.models import Question

# redirect
from flask import url_for
from werkzeug.utils import redirect

bp = Blueprint('main',__name__,url_prefix='/')

# @bp.route('/')
# def main_hello():
#     return 'BP main_hello'

@bp.route('/page1')
def page1_hello():
    return 'BP page1_hello'


# ----------------------------------------------bp로 분기해줌,----------------------------------------------------
# -------------------------------main으로 들어올 시 question/list redirect 하게함----------------------------------

@bp.route('/')
def index():
    
    # 'question' 이라는 bp의 q_list()로 접근해라 
    return redirect(url_for('question.q_list'))


# # web 페이지로 보이게 해줌
# # web 페이지에 입려된 데이터 보여주기
# @bp.route('/web')
# def index():
    
#     # create_date column기준으로 정렬해서 가져오기
#     q_list = Question.query.order_by(Question.create_date.desc())

#     print(q_list)
#     # Jinja2 덕분에 html에 변수 선언,조건문을 통해 작성할 수 있음
#     return render_template('q_list/q_list.html',q_list=q_list)

#     # 이후 템플릿을 만들어줌
#     # service1/templates에 만들기
#     # service1/templates/q_list/q_list.html 만들기
#     # html 파일에 jinja2 문법으로 작성

# # q_list.html에서 링크누르면 이동
# @bp.route('/detail/<int:q_id>/')
# def detail(q_id):
#     print("체크 q_id :",q_id)
    
#     # 페이지가 없을 시 404 오류 뜨게함 
#     question = Question.query.get_or_404(q_id)  
#     question = Question.query.get(q_id)
#     return render_template('q_list/q_detail.html',question=question)
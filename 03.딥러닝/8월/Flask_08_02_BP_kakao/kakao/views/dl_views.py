from flask import Blueprint

bp = Blueprint('dl',__name__,url_prefix='/dl')


@bp.route('/prj1')
def kakao_chat():
    return '(bp) dl_prj1 \n 딥러닝 프로젝트입니다.'

@bp.route('/prj2')
def kakao_ml():
    return '(bp) dl_prj2 \n 딥러닝 프로젝트2입니다.'
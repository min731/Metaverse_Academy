from flask import Blueprint

# blueprint 하나로 처리할지 여러개로 처리할지
# blueprint 이름이 같으면 안됌
bp = Blueprint('classification',__name__,url_prefix='/classification')

# 127.0.0.1:5000/classification/catdog
@bp.route('/catdog')
def classification_catdog():
    return '(bp) 고양이입니다.'

@bp.route('/birdflower')
def classification_birdflower():
    return '(bp) 비둘기입니다.'

@bp.route('/manwoman')
def classification_manwoman():
    return '(bp) 여성입니다.'
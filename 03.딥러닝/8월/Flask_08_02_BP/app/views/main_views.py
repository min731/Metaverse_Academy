from flask import Blueprint

# url_prefix 주소에 들어오면 bp가 받음
bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def hello_pybo():
    return '(bp) Hello, Pybo!'

@bp.route('/meta')
def hello_meta():
    return '(bp) 메타버스아카데미 ai'
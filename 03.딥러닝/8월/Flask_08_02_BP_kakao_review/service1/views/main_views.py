from flask import Blueprint


bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def main_hello():
    return 'BP main_hello'

@bp.route('/page1')
def page1_hello():
    return 'BP page1_hello'
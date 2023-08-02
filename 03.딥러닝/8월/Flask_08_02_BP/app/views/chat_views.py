from flask import Blueprint

# blueprint 하나로 처리할지 여러개로 처리할지
# blueprint 이름이 같으면 안됌
bp = Blueprint('chat',__name__,url_prefix='/chat')

# 127.0.0.1:5000/classification/catdog
@bp.route('/chatgpt')
def chat_chatgpt():
    return '(bp) chatgpt입니다.'

@bp.route('/lama2')
def chat_lama2():
    return '(bp) lama2입니다.'

from service1 import db

# DB는 보통 models.py로 씀

# ORM
# 테이블을 만들때 클래스로 만들면 됌

# class 테이블명
class Question(db.Model):

    # 컬럼명
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(),nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    # 몇번 질문에 대한 답인지
    # ForeignKey : 다른 테이블에서 PK로 쓰는 키를 가져옴
    # ondelete='CASCADE' : 질문이 삭제되면 답변도 삭제함
    question_id = db.Column(db.Integer, db.ForeignKey('question.id',ondelete='CASCADE'))

    # 같은 답변들을 끼리 묶어주는 역할

    # answer_set : 입력된 답변을 질문에 묶어주게함
    question = db.relationship('Question',backref=db.backref('answer_set'))
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(),nullable=False)

    # 새 테이블 만들고 
    # flask db migrate 
    # 버전이 생김

    # 새 버전으로 바꿔줌
    # flask db upgrade
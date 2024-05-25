from flask import Blueprint

#첫 번째 인 수 main 은 블루프린트의 별칭이다.
bp = Blueprint('main',__name__,url_prefix='/')


@bp.route('/hello')
def hello_world():
    return 'Hello, world!'

@bp.route('/')
def index():
    return 'Pybo index'
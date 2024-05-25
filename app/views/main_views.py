from flask import Blueprint, url_for
from werkzeug.utils import redirect


#첫 번째 인 수 main 은 블루프린트의 별칭이다.
bp = Blueprint('main',__name__,url_prefix='/')


@bp.route('/hello')
def hello_world():
    return 'Hello, world!'


#url_for('블루프린트 명칭',블루프린트 등록된 함수명) -> 라우팀함수를 찾는다.
@bp.route('/')
def index():
    return redirect(url_for('question._list'))
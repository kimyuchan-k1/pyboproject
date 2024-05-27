from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
from sqlalchemy import MetaData


#sqlite3의 문제 해결.. flask ORM 을 사용하기 위함데이터베이스에서 
#디폴트 값으로 명명되던 프라이머리 키, 유니크 키 등의 제약조건 이름을 수동으로 설정한 것이다.
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


# 다른 모듈에서 사용할 수 있게 전역변수로 지정




# create app 은 애플리케이션 팩토리이고 플라스크 내에서 정의된 함수명이다. 즉 바꾸면 동작하지 않음.
def create_app():
    app = Flask(__name__)
    #config파일을 읽기위함.
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models


    # 블루프린트를 가져와서 등록함.
    from .views import main_views,question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    #filter
    from .filter import format_datetime
    #jinja 문법에 적용하기 위해 필터를 적용
    app.jinja_env.filters['datetime'] = format_datetime



    return app
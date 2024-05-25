from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

# 다른 모듈에서 사용할 수 있게 전역변수로 지정

# from app import db 혹은 migrate로 import 한다.
db = SQLAlchemy()
migrate = Migrate()





# create app 은 애플리케이션 팩토리이고 플라스크 내에서 정의된 함수명이다. 즉 바꾸면 동작하지 않음.
def create_app():
    app = Flask(__name__)
    #config파일을 읽기위함.
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models


    # 블루프린트를 가져와서 등록함.
    from .views import main_views,question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    return app
from flask import Flask


# create app 은 애플리케이션 팩토리이고 플라스크 내에서 정의된 함수명이다. 즉 바꾸면 동작하지 않음.
def create_app():
    app = Flask(__name__)


    # 블루프린트를 가져와서 등록함.
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
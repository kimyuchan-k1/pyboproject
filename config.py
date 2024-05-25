import os


#db 초기설정

BASE_DIR = os.path.dirname(__file__)

# uri 는 db 접속 주소이다.
#sqlite 데이터베이스가 사용되고 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장된다.
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))

# sqlalchemy 의 이벤트 처리하는 옵션을 비활성화함
SQLALCHEMY_TRACK_MODIFICATIONS =False

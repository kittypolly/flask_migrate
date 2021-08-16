#절대 경로를 위한 import다.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#migrate를 사용하는 이유
#데이터베이스에 새로운 컬럼을 추가하는 등의 변화를 주고 업데이트를 하기위해 migrate를 사용합니다.
#데이터베이스를 설정하고 열을 추가하는데 python으로 구현하는 것보다 migrate를 사용하는게 더 쉽다.
#아래는 터미널에 타이밍해야하는 내용이다.
#1. pip install Flask-Migrate
#2. export FLASK_APP=[myapp].py (여기서는 main.py를 사용한다.) #안되면 export 대신에 set을 입력해보자. 띄어쓰기 없이 해야한다.
#3. flask db init # migrations라는 폴더가 생긴다.
#4. flask db migrate -m "[commit내용]"
#5. flask db upgrade 

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)


class AOA(db.Model):
    
    __table__name = "AOA"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    birth = db.Column(db.Integer)
    #migrate가 작동하는 것을 보기 위해서 height column을 추가하였다.
    #터미널에 flask db migrate "add height column"을 타이핑한다.
    #그리고 falsk db upgrade를 타이핑한다.
    height = db.Column(db.Integer)

    def __init__(self, name, birth, height):
        self.name = name
        self.birth = birth
        self.height = height

    def __repr__(self):
        return f"AOA의 멤버 {self.name}의 출생년도는 {self.birth}년 입니다."
    
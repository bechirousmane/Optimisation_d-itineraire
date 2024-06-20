from  flask import Flask
from config import Config
from api.data_base.src.models import db, User
from api.data_base.src.dbApi import DBApi
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

with  app.app_context() :
    db_api = DBApi()
    db_api.start()
    birth_date = datetime.strptime('2001-01-17', '%Y-%m-%d').date()
    user = User(id=1, name='Bechir', firstname='ousmane', birth=birth_date, email='obechir@gmail.com')
    user.set_password('bebebe')
    db.session.add(user)
    db.session.commit()

    bechir = db.session.query(User).filter(User.id==1).first()
    print(f"the user {bechir.name} {bechir.firstname} birth {bechir.birth} with email {bechir.email} and password {bechir.password_hash}")
    
if __name__=='__main__' :
    app.run(debug=True)
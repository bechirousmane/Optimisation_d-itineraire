from flask import Flask
from flask_restful import Api
from config import Config
from api.src.data_base.models import db, User
from api.src.data_base.dbApi import DBApi
from api.src.rest.schemas import ma
from api.src.rest.resources import *
from datetime import datetime 



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
ma.init_app(app)

api = Api(app)
api.add_resource(ItineraryResource, '/itineraries', '/itinerary/<int:itinerary_id>')


with  app.app_context() :
    db_api = DBApi()
    db_api.start()
    birth_date = datetime.strptime('2001-01-17', '%Y-%m-%d').date()
    user = User(id=1, name='BECHIR', firstname='ousmane', birth=birth_date, email='obechir@gmail.com')
    user.set_password('bebebe')
    db.session.add(user)
    db.session.commit()
    itineraire1 = Itinerary(id=1, id_user=1, name='itineraire1')
    itineraire2 = Itinerary(id=2, id_user=1, name='itineraire2')
    db.session.add(itineraire1)
    db.session.add(itineraire2)
    db.session.commit()

    bechir = db.session.query(User).filter(User.id==1).first()
    print(f"the user {bechir.name} {bechir.firstname} birth {bechir.birth} with email {bechir.email} and password {bechir.password_hash}")
    
if __name__=='__main__' :
    app.run()

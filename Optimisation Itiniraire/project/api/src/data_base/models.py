from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()
db = SQLAlchemy(model_class=Base)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    birth = Column(Date, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    itineraries = relationship('Itinerary', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Itinerary(Base):
    __tablename__ ='itineraries'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(255), nullable=False)
    user = relationship('User', back_populates='itineraries')
    breakpoints = relationship('BreakPoint', back_populates='itinerary')

class BreakPoint(Base):
    __tablename__ ='breakpoints'
    id = Column(Integer, primary_key=True)
    id_itinerary = Column(Integer, ForeignKey('itineraries.id'), nullable=False)
    name = Column(String(255), nullable=False)
    geoloc = Column(String(255), nullable=False)
    itinerary = relationship('Itinerary', back_populates='breakpoints')

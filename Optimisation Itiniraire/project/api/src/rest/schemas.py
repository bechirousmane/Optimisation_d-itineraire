from flask_marshmallow import Marshmallow
from api.src.data_base.models import User, Itinerary, BreakPoint

ma  = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema) :

    class Meta :
        model = User()

class ItinerarySchema(ma.SQLAlchemyAutoSchema) :

    class Meta :
        model = Itinerary()

class BreakPointSchema(ma.SQLAlchemyAutoSchema) :

    class Meta :
        model = BreakPoint()
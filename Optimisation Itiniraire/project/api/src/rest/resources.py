from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from schema import *
from data_base.models import *

class ItineraryResource(Resource) : 
    itinerary_schema = ItinerarySchema()
    itineraries_schema = ItinerarySchema(many=True)

    def get(self,itinerary_id=None) :
        if itinerary_id :
            itinerary = Itinerary.query.get_or_404(itinerary_id)
            return self.itinerary_schema.dump(itinerary)
        
        else :
            all_itineraries = Itinerary.query.all()
            return self.itineraries_schema.dump(all_itineraries)
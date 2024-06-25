from config import Config
from api.src.data_base.models import db

class DBApi: 

    def start(self):
        try:
            db.drop_all()
            db.create_all()
        except Exception as e:
            print(f"Error creating tables: {e}")

    



from sqlalchemy import create_engine
from config import Config
from models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DBApi: 
    def __init__(self):
        self.engine = create_engine(Config.DB_URL)
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def start(self):
        try:
            Base.metadata.create_all(bind=self.engine)
        except Exception as e:
            print(f"Error creating tables: {e}")

    def get_session(self):
        return self.Session()



import os

class Config:

    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
    DATA_BASE = os.getenv('DB')
    DATA_BASE_NAME = os.getenv('DB_NAME')
    DB_URL = os.getenv('DB_URL', 'sqlite:///mydatabase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
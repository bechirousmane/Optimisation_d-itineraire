import os

class Config:

    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
    DATA_BASE = os.getenv('DB')
    DATA_BASE_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
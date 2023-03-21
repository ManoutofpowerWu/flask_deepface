"""Default configuration

Use env var to override
"""
import os

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEEPFACE_TEMP_IMAGE_PATH = os.getenv("DEEPFACE_TEMP_IMAGE_PATH")

print("Set Deepface temp image path to " + DEEPFACE_TEMP_IMAGE_PATH)
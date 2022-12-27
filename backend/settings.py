from decouple import config

SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL")
SECRET_KEY = config("SECRET_KEY")

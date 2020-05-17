import  os

os.environ['FLASK_ENV'] = 'development'
DEBUG = True


SQLALCHEMY_DATABASE_URI = 'sqlite:///../mytwt.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
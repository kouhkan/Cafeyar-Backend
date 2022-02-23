import os


class Base(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATION', False)
    SECRET_KEY = os.getenv('SECRET_KEY')


class Development(Base):
    pass


class Production(Base):
    pass
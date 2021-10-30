import os


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', None)

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'orders.db')

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'  # :memory:
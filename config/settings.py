import os

SECRET_KEY = os.getenv('SECRET_KEY', None)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'orders.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
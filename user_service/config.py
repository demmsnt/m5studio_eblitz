import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Config
SECRET_KEY = os.getenv('SECRET_KEY')

# DB
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(
    os.getenv('POSTGRES_USER'),
    os.getenv('POSTGRES_PASSWORD'),
    os.getenv('POSTGRES_HOST'),
    os.getenv('POSTGRES_DB'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
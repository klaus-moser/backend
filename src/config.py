from os import environ, getenv
from datetime import timedelta
from dotenv import load_dotenv


load_dotenv()

modes: dict = {'PRODUCTION': 'ProductionConfig',
               'DEVELOP': 'DevelopmentConfig',
               'TEST': 'TestingConfig'}


class Config(object):
    """
    Default configuration.
    """
    ADMIN: int = 1

    ENV = 'production'
    DEBUG = False
    TESTING = False
    SECRET_KEY = getenv('SECRET_KEY')

    DB_NAME = "production-db"
    DB_USERNAME = getenv('DB_USERNAME')
    DB_PASSWORD = getenv('DB_PASSWORD')

    SESSION_COOKIE_SECURE = True

    FLASK_SERVER_NAME = 'localhost:5000'
    FLASK_THREADED = True

    JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=120)
    JWT_COOKIE_SECURE = False
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=15)
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True

    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///' + DB_NAME + '.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True


class ProductionConfig(Config):
    """
    Production configuration.
    """
    pass


class DevelopmentConfig(Config):
    """
    Development configuration.
    """
    ENV = 'development'
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = getenv('DB_USERNAME_DEV')
    DB_PASSWORD = getenv('DB_PASSWORD_DEV')

    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///' + DB_NAME + '.db')

    SESSION_COOKIE_SECURE = False

    LOG_LEVEL = 'DEBUG'


class TestingConfig(Config):
    """
    Testing configuration.
    """
    ENV = 'testing'
    TESTING = True

    DB_NAME = "testing-db"
    DB_USERNAME = getenv('DB_USERNAME_DEV')
    DB_PASSWORD = getenv('DB_PASSWORD_DEV')

    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///' + DB_NAME + '.db')

    SESSION_COOKIE_SECURE = False

    LOG_LEVEL = 'DEBUG'

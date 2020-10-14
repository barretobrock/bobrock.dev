import os


class Config(object):
    """
    Default config
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./database.db'
    SECRET_KEY = os.environ['BOBDEV_SECRET_KEY']
    REGISTER_KEY = os.environ['REGISTRATION_KEY']


class BaseConfig(Config):
    """
    Base config class
    """
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    """
    Production-specific config
    """
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """
    Development-specific config
    """
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True

import os
base_dir = os.path.abspath(os.path.dirname(__file__))


def get_local_secret(path: str) -> str:
    """Grabs a locally-stored secret for debugging"""
    with open(path) as f:
        return f.read().strip()


class Config(object):
    """
    Default config
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(base_dir, "database.db")}'
    SECRET_KEY = os.environ.get('BOBDEV_SECRET_KEY')
    REGISTER_KEY = os.environ.get('REGISTRATION_KEY')
    STATIC_DIR_PATH = '../static'
    TEMPLATE_DIR_PATH = '../templates'


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
    SECRET_KEY = get_local_secret(os.path.join(base_dir, *['secrets', 'bobdev_secret']))
    REGISTER_KEY = get_local_secret(os.path.join(base_dir, *['secrets', 'register']))
    STATIC_DIR_PATH = '../static'
    TEMPLATE_DIR_PATH = '../templates'

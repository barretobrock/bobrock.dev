from configurations import ProductionConfig
# Internal packages
from routes import create_app


if __name__ == "__main__":
    application = create_app(config_class=ProductionConfig)
    application.run()

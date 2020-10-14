from configurations import ProductionConfig
# Internal packages
from routes import create_app


if __name__ == "__main__":
    app = create_app(config_class=ProductionConfig)
    app.run()

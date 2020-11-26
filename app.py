from flask import Flask
from dotenv import load_dotenv
import os

from routes.register_routes import register as register_routes
from factories.config import ConfigFactory
from database import SingletonDB

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app


def setup_config(app):
    load_dotenv()
    environment = os.environ['ENVIRONMENT']
    config = ConfigFactory.create(environment)
    app.config.from_object(config)


def setup_database(app):
    SingletonDB(app)


if __name__ == '__main__':
    app = create_app()
    setup_config(app)
    setup_database(app)
    app.run()
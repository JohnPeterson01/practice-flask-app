from flask import Flask
from dotenv import load_dotenv
import os

from routes.register_routes import register as register_routes
from factories.config import ConfigFactory
from dependencies import MainApp, MainDatabase


def create_app():
    app_obj = MainApp.app()
    # Retrieving the application property from the main app object
    app = app_obj.application
    register_routes(app)
    return app


def setup_config(app):
    load_dotenv()
    environment = os.environ['ENVIRONMENT']
    config = ConfigFactory.create(environment)
    app.config.from_object(config)


def setup_database():
    MainDatabase.database()


if __name__ == '__main__':
    app = create_app()
    setup_config(app)
    setup_database()
    app.run()
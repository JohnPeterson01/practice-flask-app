from flask import Flask
from dotenv import load_dotenv
import os

from routes.register_routes import register as register_routes
from factories.config import ConfigFactory
from dependencies import MainApp, MainDatabase


def create_app():
    app = MainApp.application()
    register_routes(app)
    return app


def setup_config(app_obj):
    load_dotenv()
    environment = os.environ['ENVIRONMENT']
    config = ConfigFactory.create(environment)
    app_obj.app.config.from_object(config)


def setup_database():
    MainDatabase.database()


if __name__ == '__main__':
    app_obj = create_app()
    setup_config(app_obj)
    setup_database()
    app_obj.app.run()
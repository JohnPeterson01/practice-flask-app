import os
from dotenv import load_dotenv

from src.dependencies import MainApp, \
    MainDatabase, \
    RouteRegistries, \
    Config
from src.session import configure_session_factory


def create_app(testing=False):
    load_dotenv()

    app = MainApp.application().app
    setup_config(app)
    setup_database(testing)
    setup_routes()

    app_name = get_app_name()
    # Test the configure session factory piece
    configure_session_factory(app, app_name, testing)
    app.run()


def get_app_name():
    # os.environ['APP_NAME']
    return 'user-service'


def setup_routes():
    RouteRegistries.user_routes_registry()


def setup_config(app):
    config_obj = Config.config_factory()
    app.config.from_object(config_obj.config)


def setup_database(testing):
    MainDatabase.database(testing=testing)


# TODO: move into separate file
def runserver():
    create_app()

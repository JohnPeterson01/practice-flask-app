import os
from dotenv import load_dotenv

from src.dependencies import MainApp, \
    RouteRegistries, \
    Config
from src.session import configure_session_factory
from src.setup.create_all import main as createall_main
from src.setup.drop_all import main as drop_all_main


def create_app(testing=False, run_app=True):
    app = MainApp.application().app
    setup_config(app)
    setup_routes()

    app_name = get_app_name()
    # Test the configure session factory piece
    configure_session_factory(app, app_name, testing)
    if run_app:
        app.run()
    return app

def get_app_name():
    load_dotenv()
    return os.environ['APP_NAME']


def setup_routes():
    RouteRegistries.user_routes_registry()


def setup_config(app):
    config_obj = Config.config_factory()
    app.config.from_object(config_obj.config)


# TODO: move into separate file
def runserver():
    create_app()


def createall():
    testing = False
    create_app(testing, run_app=False)
    app_name = get_app_name()
    createall_main(app_name, testing)


def dropall():
    testing = False
    create_app(testing, run_app=False)
    app_name = get_app_name()
    drop_all_main(app_name, testing)
    
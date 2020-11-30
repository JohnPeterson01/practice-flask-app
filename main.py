from dependencies import MainApp, \
    MainDatabase, \
    RouteRegistries, \
    Config


def create_app():
    app = MainApp.application()
    return app


def setup_routes():
    RouteRegistries.user_routes_registry()


def setup_config(app_obj):
    config_obj = Config.config_factory()
    app_obj.app.config.from_object(config_obj.config)


def setup_database():
    MainDatabase.database()


if __name__ == '__main__':
    app_obj = create_app()
    setup_config(app_obj)
    setup_database()
    setup_routes()
    app_obj.app.run()
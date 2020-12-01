from flask.blueprints import Blueprint


class RoutesRegistry(Blueprint):
    def __init__(self, blueprint_name, application, routes, url_prefix):
        super().__init__(blueprint_name, __name__)

        self.app = application.app
        self.routes = routes
        self.url_prefix = url_prefix

        self._register_routes()
        self._register_blueprint()

    def _register_routes(self):
        self.routes.register(self)

    def _register_blueprint(self):
        self.app.register_blueprint(self, url_prefix=self.url_prefix)






# from routes.user_routes import user_blueprint

# Convert to registry class
# def register(app_obj):
#     app = app_obj.app
#     app.register_blueprint(user_blueprint, url_prefix="/api/v1/user")

# from routes.user.user_routes import UserRoutes


class RoutesRegistry:
    def __init__(self, application, user_blueprint, user_routes, user_store):
        self.app = application.app
        # User route specific
        self.user_blueprint = user_blueprint
        self.user_routes = user_routes
        self.user_store = user_store
        self._register_routes()

    def _register_routes(self):
        self.app.register_blueprint(self.user_blueprint, url_prefix="/api/v1/user")
        

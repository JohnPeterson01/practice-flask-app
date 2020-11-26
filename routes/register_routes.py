from routes.user_routes import user_blueprint


def register(app):
    app.register_blueprint(user_blueprint, url_prefix="/api/v1/user")

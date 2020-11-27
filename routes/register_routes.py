from routes.user_routes import user_blueprint


# Convert to registry class
def register(app_obj):
    app = app_obj.app
    app.register_blueprint(user_blueprint, url_prefix="/api/v1/user")


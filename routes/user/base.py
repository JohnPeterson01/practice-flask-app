from flask.blueprints import Blueprint


class UserRoutesBlueprint(Blueprint):
    def __init__(self):
        super().__init__('user_blueprint', __name__)
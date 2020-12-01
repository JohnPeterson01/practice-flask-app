from flask_sqlalchemy import SQLAlchemy


class DatabaseStore:
    def __init__(self, application):
        app = application.app
        self.db = SQLAlchemy(app)





from flask_sqlalchemy import SQLAlchemy


# Singleton class for the database
class SingletonDB:
    class __DB:
        def __init__(self, app):
            self.db = SQLAlchemy(app)
    instance = None

    def __init__(self, app=None):
        if app and not SingletonDB.instance:
            SingletonDB.instance = SingletonDB.__DB(app)






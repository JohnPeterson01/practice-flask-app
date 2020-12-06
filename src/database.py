from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine as create_sqlalchemy_engine


class DatabaseStore:
    def __init__(self, application, testing):
        app = application.app
        self.db = SQLAlchemy(app)


def convert_dashes_to_underscores(old_name):
    return old_name.replace('-','_')


def select_database_name(app_name, testing):
    underscored_app_name = convert_dashes_to_underscores(app_name)
    if testing:
        return f'{underscored_app_name}_test'
    else:
        return underscored_app_name


def create_engine(app_name, testing):
    database_name = select_database_name(app_name, testing)
    return create_sqlalchemy_engine(f'postgresql://user:user@localhost:5432/{database_name}')

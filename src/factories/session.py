from sqlalchemy.orm import sessionmaker
from src.database import create_engine

from src.factories.base import BaseCreator


class SessionMakerFactory(BaseCreator):
    def __init__(self, app_name, testing):
        self.app_name = app_name
        self.testing = testing

    def create(self):
        engine = create_engine(self.app_name, self.testing)
        return sessionmaker(bind=engine)


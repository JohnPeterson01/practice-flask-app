from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from factories.base import BaseCreator


class DatabaseSessionFactory(BaseCreator):
    def create():
        engine = create_engine("postgresql://root:root@localhost:5432/random", echo=True)
        session = sessionmaker(bind=engine)
        return session
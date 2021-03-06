from src.models.base import ModelBase
from sqlalchemy import Column, Integer, String


class UserModel(ModelBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User(name='%s', email='%s')>" % (
            self.name, self.email)
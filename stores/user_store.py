from .base import BaseCRUDStore
from database import SingletonDB

from models.user_model import UserModel


# Dependency on the db and on the
class UserStore(BaseCRUDStore):
    def __init__(self):
        self.model = UserModel
        self.db = SingletonDB.instance.db

    def create(self, creation_dict):
        model_obj = self.model(**creation_dict)
        self.db.session.add(model_obj)
        self.db.session.commit()
        return

    def search_all(self):
        users = self.db.session.query(UserModel)
        return users



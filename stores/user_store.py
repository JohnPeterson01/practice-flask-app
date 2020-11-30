from .base import BaseCRUDStore

from models.user_model import UserModel


class UserStore(BaseCRUDStore):
    def __init__(self, database):
        self.model = UserModel
        self.db = database.db

    def create(self, creation_dict):
        model_obj = self.model(**creation_dict)
        self.db.session.add(model_obj)
        self.db.session.commit()
        return

    def search_all(self):
        users = self.db.session.query(self.model)
        return users



from .base import BaseCRUDStore
from database import SingletonDB

from models.user_model import UserModel


# Dependency on the db and on the
class UserStore(BaseCRUDStore):
    def __init__(self):
        print('initialising UserStore')
        self.model = UserModel
        self.db = SingletonDB.instance.db

    def create(self, creation_dict):
        print('creating a user obj')
        breakpoint()
        model_obj = self.model(**creation_dict)
        self.db.session.add(model_obj)
        self.db.session.commit()
        print('finished inserting user into the database')
        return

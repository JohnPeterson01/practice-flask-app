import json

from src.stores.base import BaseCRUDStore
from src.models.user_model import UserModel


class UserStore(BaseCRUDStore):
    def __init__(self, database, cache):
        self.model = UserModel
        self.db = database.db
        self.cache = cache

    def create(self, creation_dict):
        model_obj = self.model(**creation_dict)
        self.db.session.add(model_obj)
        self.db.session.commit()
        return

    # TODO: Implement cache as a decorator
    def search_all(self):

        cache_operation = 'searchall'
        cache_result = self.cache.get(cache_operation)

        if cache_result is None:
            users = self.db.session.query(self.model)
            users_arr = self._parse_db_results(users)
            self.cache.set(cache_operation, json.dumps(users_arr))
            return users_arr
        else:
            users_arr = self._parse_cache_result(cache_result)
            return users_arr

    # TODO: Implement filter by user_id

    # TODO: Move this to parent class
    def _parse_db_results(self, raw_results):
        results_arr = []
        # Make this less manual
        for user in raw_results:
            user_obj = {
                "name": user.name,
                "email": user.email
            }
            results_arr.append(user_obj)
        return results_arr

    # TODO: Move to cache class
    def _parse_cache_result(self, raw_result):
        return json.loads(raw_result.decode())





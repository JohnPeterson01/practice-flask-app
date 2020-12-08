import json

from src.stores.base import BaseCRUDStore
from src.models.user_model import UserModel


class UserStore(BaseCRUDStore):
    def __init__(self, cache):
        self.model = UserModel
        self.cache = cache
        self.filter_fields = {
                "id": UserModel.id,
                "name": UserModel.name,
                "email": UserModel.email
        }

    def create(self, creation_dict):
        model_obj = self.model(**creation_dict)
        self.session.add(model_obj)
        self.session.commit()
        return

    def search_all(self):

        cache_operation = 'searchall'
        cache_result = self.cache.get(cache_operation)

        if cache_result is None:
            users = self.session.query(self.model)
            users_arr = self._parse_db_results(users)
            self.cache.set(cache_operation, json.dumps(users_arr))
            return users_arr
        else:
            users_arr = json.loads(cache_result)
            return users_arr

    def filter(self, **filter_dict):
        query_obj = self.session.query(self.model)

        for key, value in filter_dict.items():
            model_field = self.filter_fields[key]
            query_obj = query_obj.filter(model_field == value)
        
        # Need to automatically create filter's from a filter dict
        users_arr = self._parse_db_results(query_obj)

        return users_arr


    # TODO: Move this to parent class
    def _parse_db_results(self, query):
        results_arr = []
        # Make this less manual
        for user in query:
            user_obj = {
                "name": user.name,
                "email": user.email
            }
            results_arr.append(user_obj)
        return results_arr





from hamcrest import assert_that, equal_to
from unittest.mock import patch

from src.main import create_app, get_app_name
from src.helpers.create_all import main as createall_main
from src.helpers.drop_all import main as drop_all_main

from src.dependencies import Stores, Caches
from src.context import SessionContext


class TestUserStore:

    def setup(self):

        testing = True
        self.app = create_app(testing, run_app=False)

        # Drop all tables, then create
        app_name = get_app_name()
        drop_all_main(app_name, testing)
        createall_main(app_name, testing)

        self.store = Stores.user_store()
        self.session = SessionContext.make(app_name, testing)
        self.base_cache = Caches.redis()

    def teardown(self):
        self.session.close()
        self.base_cache.flush_all()

    def test_successful_add_record_to_database(self):
        # Arrange, act, assert
        user_to_create = {
            "name": "Bob",
            "email": "bob@gmail.com"
        }
        db_result = self.store.create(user_to_create)

        assert_that(db_result, equal_to(None), 'assertion error')

    def test_successful_retrieval_from_database_using_single_filter(self):
        user_to_create = {
            "name": "Bob",
            "email": "bob@gmail.com"
        }
        self.store.create(user_to_create)

        filter_dict = {"id": 1, "name": "Bob"}
        db_result = self.store.filter(**filter_dict)
        expected_result = [user_to_create]

        assert_that(db_result, equal_to(expected_result), 'assertion error')


    def test_successful_retrieval_from_database_using_multiple_filters(self):
        user_to_create_1 = {
            "name": "Bob",
            "email": "bob@gmail.com"
        }
        user_to_create_2 = {
            "name": "James",
            "email": "james@gmail.com"
        }
        self.store.create(user_to_create_1)
        self.store.create(user_to_create_2)

        filter_dict = {"id": 2, "name": "James"}
        db_result = self.store.filter(**filter_dict)
        expected_result = [user_to_create_2]
        assert_that(db_result, equal_to(expected_result), 'assertion error')

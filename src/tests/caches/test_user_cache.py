from hamcrest import assert_that, equal_to
from unittest.mock import patch

from src.main import create_app
from src.dependencies import Caches


class TestUserCache:

    def setup(self):

        self.app = create_app(testing=True, run_app=False)
        self.cache = Caches.user_cache()
        self.base_cache = Caches.redis()

    def teardown(self):
        self.base_cache.flush_all()

    def test_adding_string_value_to_cache(self):
        operation_name = 'searchall'
        value = 'bob'
        response = self.cache.set(operation_name, value)
        assert_that(response, equal_to(None), 'assertion error')

    def test_set_and_get_string_value_from_cache(self):
        operation_name = 'searchall'
        value = 'bob'
        self.cache.set(operation_name, value)
        retrieved_value = self.cache.get(operation_name)
        assert_that(retrieved_value, equal_to(value), 'assertion error')

    def test_set_and_get_value_with_filter_function_arguments(self):
        operation_name = 'filter'
        value = 'bob'
        filter_value_1 = 3
        filter_value_2 = 2
        filter_value_3 = 5
        self.cache.set(operation_name, value, filter_value_1, filter_value_2, filter_value_3)
        retrieved_value = self.cache.get(operation_name, filter_value_1, filter_value_2, filter_value_3)
        assert_that(retrieved_value, equal_to(value), 'assertion error')
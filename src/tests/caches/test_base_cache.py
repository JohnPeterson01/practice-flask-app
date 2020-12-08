from hamcrest import assert_that, equal_to
from unittest.mock import patch

from src.main import create_app
from src.dependencies import Caches


class TestUserCache:

    def setup(self):
        self.app = create_app(testing=True, run_app=False)
        self.cache = Caches.redis()

    def test_flushing_entire_cache(self):
        key_1 = 'name1'
        value_1 = 'bob'
        self.cache.set(key_1, value_1)

        key_2 = 'name2'
        value_2 = 'james'
        self.cache.set(key_2, value_2)

        # Flush cache
        self.cache.flush_all()

        retrieved_value_1 = self.cache.get(key_1)
        assert_that(retrieved_value_1, equal_to(None), 'assertion error')

        retrieved_value_2 = self.cache.get(key_2)
        assert_that(retrieved_value_2, equal_to(None), 'assertion error')

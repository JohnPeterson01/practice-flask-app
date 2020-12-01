from hamcrest import assert_that, equal_to
from unittest.mock import patch


class TestUserCache:
    
    def setUp(self):
        self.cache = {}
    
    def test_adding_value_to_cache(self):
        assert_that(True, equal_to(False), 'assertion error')
from hamcrest import assert_that, equal_to
from unittest.mock import patch

from src.main import create_app


class TestUserCache:
    
    def setUp(self):
        self.app = create_app(testing=True, run_app=False)
    
    def test_adding_value_to_cache(self):
        assert_that(True, equal_to(False), 'assertion error')
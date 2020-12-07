from hamcrest import assert_that, equal_to
from unittest.mock import patch

from src.main import create_app, get_app_name
from src.helpers.create_all import main as createall_main
from src.helpers.drop_all import main as drop_all_main


class TestUserStore:

    def setUp(self):

        testing = True
        self.app = create_app(testing, run_app=False)
        
        # Drop all tables, then create
        app_name = get_app_name()
        drop_all_main(app_name, testing)
        createall_main(app_name, testing)



    def teardown(self):
        pass

    def test_add_record_to_database(self):
        assert_that(True, equal_to(False), 'assertion error')
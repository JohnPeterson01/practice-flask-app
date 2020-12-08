from hamcrest import assert_that, equal_to, is_, has_entries, contains
from unittest.mock import patch

from src.main import create_app, get_app_name
from src.helpers.create_all import main as createall_main
from src.helpers.drop_all import main as drop_all_main

from src.dependencies import Caches
# from src.context import SessionContext


class TestUserRoutes:

    def setup(self):
        self.testing = True
        self.app = create_app(self.testing, run_app=False)
        self.client = self.app.test_client()
        self.base_uri = 'api/v1/user'

        # Drop all tables, then create
        self.app_name = get_app_name()
        drop_all_main(self.app_name, self.testing)
        createall_main(self.app_name, self.testing)

        self.base_cache = Caches.redis()

    def teardown(self):
        self.base_cache.flush_all()

    def test_create_user(self):
        uri = f'{self.base_uri}/new'
        response = self.client.post(
            uri,
            json=dict(
                name="Bob",
                email="bob@gmail.com"
            ),
        )
        assert_that(response.status_code, is_(equal_to(201)))

    def test_no_users_added_search_all(self):
        uri = f'{self.base_uri}/all'
        response = self.client.get(uri)

        assert_that(response.status_code, is_(equal_to(200)))
        assert_that(
            response.json,
            has_entries(
                results=[]
            ),
        )

    def test_single_user_added_search_all(self):
        uri_create_user = f'{self.base_uri}/new'
        user_name_1 = "Bob"
        user_email_1 = "bob@gmail.com"
        self.client.post(
            uri_create_user,
            json=dict(
                name=user_name_1,
                email=user_email_1
            ),
        )

        uri = f'{self.base_uri}/all'
        response = self.client.get(uri)

        assert_that(response.status_code, is_(equal_to(200)))
        assert_that(
            response.json,
            has_entries(
                results=contains(
                    has_entries(
                        name=user_name_1,
                        email=user_email_1
                    ),
                ),
            ),
        )

    def test_filter_user_by_id(self):
        uri_create_user = f'{self.base_uri}/new'
        user_name_1 = "Bob"
        user_email_1 = "bob@gmail.com"
        self.client.post(
            uri_create_user,
            json=dict(
                name=user_name_1,
                email=user_email_1
            ),
        )

        user_id = 1
        uri = f'{self.base_uri}/{user_id}'
        response = self.client.get(uri)

        assert_that(response.status_code, is_(equal_to(200)))
        assert_that(
            response.json,
            has_entries(
                results=contains(
                    has_entries(
                        name=user_name_1,
                        email=user_email_1
                    ),
                ),
            ),
        )

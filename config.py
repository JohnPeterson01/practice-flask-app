import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        self._load_from_env_file()
        self.DEBUG = False
        self.TESTING = False
        self.CSRF_ENABLED = True
        self.SECRET_KEY = 'this-really-needs-to-be-changed'

    def _load_from_env_file(self):
        load_dotenv()


class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self.SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.DEVELOPMENT = True
        self.DEBUG = True


class TestConfig(Config):
    def __init__(self):
        super().__init__()
        self.DEVELOPMENT = False
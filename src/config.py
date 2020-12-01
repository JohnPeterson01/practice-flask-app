import os


class Config:
    def __init__(self):
        self.DEBUG = False
        self.TESTING = False
        self.CSRF_ENABLED = True
        self.SECRET_KEY = 'this-really-needs-to-be-changed'

        self.SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        self.REDIS_HOSTNAME = os.environ['REDIS_HOSTNAME']
        self.REDIS_PORT = os.environ['REDIS_PORT']


class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.DEVELOPMENT = True
        self.DEBUG = True


class TestConfig(Config):
    def __init__(self):
        super().__init__()
        self.DEVELOPMENT = False
from config import DevelopmentConfig, TestConfig
from factories.base import BaseCreator


# Creates a config object
class ConfigFactory(BaseCreator):
    def create(type):
        if type == 'development':
            return DevelopmentConfig()
        if type == 'test':
            return TestConfig()

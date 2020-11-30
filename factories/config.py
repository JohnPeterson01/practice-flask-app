from dotenv import load_dotenv
import os

from config import DevelopmentConfig, TestConfig
from factories.base import BaseCreator


# Creates a config object
class ConfigFactory(BaseCreator):
    def __init__(self):
        load_dotenv()
        self.ENVIRONMENT = os.environ['ENVIRONMENT']
        self.config = self._load_environment_specific_config()
        
    def _load_environment_specific_config(self):

        if self.ENVIRONMENT == 'development':
            return DevelopmentConfig()
        if self.ENVIRONMENT == 'test':
            return TestConfig()

    def create(self):
        pass

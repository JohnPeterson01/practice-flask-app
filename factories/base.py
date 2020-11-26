from abc import ABC, abstractmethod


class BaseCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass
from abc import ABC, abstractmethod


class BaseCRUDStore(ABC):

    @abstractmethod
    def create(self):
        pass
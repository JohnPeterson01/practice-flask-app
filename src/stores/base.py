from abc import ABC, abstractmethod




class BaseCRUDStore(ABC):

    @abstractmethod
    def create(self):
        pass

    @property
    def session(self):
        from src.context import SessionContext
        return SessionContext.session
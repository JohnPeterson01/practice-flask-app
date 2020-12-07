from abc import ABC, abstractmethod


class BaseCRUDStore(ABC):

    @abstractmethod
    def create(self):
        pass

    @property
    def session(self):
        # Dynamic import done to prevent circular import issues
        from src.context import SessionContext
        return SessionContext.session
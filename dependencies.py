from dependency_injector import providers, containers

from stores.user_store import UserStore
from database import DatabaseStore
from app import MainApplication


class MainApp(containers.DeclarativeContainer):
    application = providers.Singleton(MainApplication)


class MainDatabase(containers.DeclarativeContainer):
    database = providers.Singleton(DatabaseStore, application=MainApp.application)


class Stores(containers.DeclarativeContainer):
    user_store = providers.Singleton(UserStore, database=MainDatabase.database)

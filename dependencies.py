from dependency_injector import providers, containers

from stores.user_store import UserStore
from database import DatabaseStore
from main_app import MainApplication


class MainApp(containers.DeclarativeContainer):
    app = providers.Singleton(MainApplication)


class MainDatabase(containers.DeclarativeContainer):
    database = providers.Singleton(DatabaseStore, app=MainApp.app)


class Stores(containers.DeclarativeContainer):
    user_store = providers.Singleton(UserStore, database=MainDatabase.database)

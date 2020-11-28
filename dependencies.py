from dependency_injector import providers, containers

from app import MainApplication
from database import DatabaseStore
from routes.registry import RoutesRegistry
from stores.user_store import UserStore
from routes.user.base import UserRoutesBlueprint
from routes.user.user_routes import UserRoutes


class MainApp(containers.DeclarativeContainer):
    application = providers.Singleton(MainApplication)


class MainDatabase(containers.DeclarativeContainer):
    database = providers.Singleton(DatabaseStore, application=MainApp.application)


class UserBlueprint(containers.DeclarativeContainer):
    user_blueprint = providers.Singleton(UserRoutesBlueprint)


class Stores(containers.DeclarativeContainer):
    user_store = providers.Singleton(UserStore, database=MainDatabase.database)


class UserRoutes(containers.DeclarativeContainer):
    user_routes = providers.Singleton(UserRoutes,
                                      user_store=Stores.user_store,
                                      user_blueprint=UserBlueprint.user_blueprint
                                      )


class RouteRegistries(containers.DeclarativeContainer):
    routes_registry = providers.Singleton(RoutesRegistry,
                                          application=MainApp.application,
                                          user_blueprint=UserBlueprint.user_blueprint,
                                          user_routes=UserRoutes.user_routes,
                                          user_store=Stores.user_store
                                          )





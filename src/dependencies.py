from dependency_injector import providers, containers

from src.app import MainApplication
from src.routes.registry import RoutesRegistry
from src.caches.base import BaseCache
from src.factories.config import ConfigFactory
from src.factories.session import SessionMakerFactory

from src.stores.user_store import UserStore
from src.routes.user.user_routes import UserRoutes
from src.caches.user_cache import UserCache


class MainApp(containers.DeclarativeContainer):
    application = providers.Singleton(MainApplication)


class Config(containers.DeclarativeContainer):
    config_factory = providers.Singleton(ConfigFactory)


class Session(containers.DeclarativeContainer):
    session_factory = providers.Singleton(SessionMakerFactory)


class Caches(containers.DeclarativeContainer):
    redis = providers.Singleton(BaseCache, config=Config.config_factory().config)
    user_cache = providers.Singleton(UserCache, base_cache=redis)


class Stores(containers.DeclarativeContainer):
    user_store = providers.Singleton(UserStore,
                                     cache=Caches.user_cache())


class Routes(containers.DeclarativeContainer):
    user_routes = providers.Singleton(UserRoutes,
                                      user_store=Stores.user_store
                                      )


class RouteRegistries(containers.DeclarativeContainer):
    user_routes_registry = providers.Singleton(RoutesRegistry,
                                               blueprint_name='user_blueprint',
                                               application=MainApp.application,
                                               routes=Routes.user_routes,
                                               url_prefix='/api/v1/user'
                                               )





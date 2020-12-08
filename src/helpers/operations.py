from sqlalchemy.exc import ProgrammingError

from src.models.base import ModelBase
from src.database import create_engine


# Implement create_all and drop_all
def create_all(app_name, testing):
    engine = create_engine(app_name, testing)
    ModelBase.metadata.create_all(engine)


def drop_all(app_name, testing):
    engine = create_engine(app_name, testing)
    ModelBase.metadata.drop_all(engine)
    drop_alembic_table(engine)


def drop_alembic_table(engine):
    try:
        engine.execute("DROP TABLE alembic_version;")
    except ProgrammingError:
        return False
    else:
        return True
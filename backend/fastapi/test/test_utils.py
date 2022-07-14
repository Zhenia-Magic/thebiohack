import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.engine.base import Connection
from sqlalchemy.future import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql.schema import Table

from app.core.db.database import Base, get_db
from app.core.db.models import Tag
from app.main import app


def insert_initial_tags(target: Table, connection: Connection, **kwargs):
    for tag in [
      "Sleep",
      "Nutrition",
      "Exercise",
      "Work",
      "Brain"
    ]:
        connection.execute(target.insert(), {"name": tag})


@pytest.fixture(scope='session', autouse=True)
def db_engine() -> Engine:
    engine = create_engine(os.environ['TEST_DATABASE_URI'])
    event.listen(Tag.__table__, "after_create", insert_initial_tags)

    Base.metadata.create_all(engine)

    yield engine

    Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(scope='function')
def db_session(db_engine: Engine) -> Session:
    """yields a SQLAlchemy connection which is rollbacked after the test"""
    session = sessionmaker(bind=db_engine, autocommit=False, autoflush=False)()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture()
def client(db_session):

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

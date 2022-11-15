from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from sqlalchemy.orm import sessionmaker, scoped_session, Session

from app.config import DatabaseConfig


class DAO:

    def __init__(self):
        self.__engine = self.__create_engine()

    #        self.__session = self.__create_session(self.__engine)()

    @staticmethod
    def __create_engine() -> Engine:
        return create_engine(
            url=DatabaseConfig.DATABASE_URL,
            encoding="utf-8",
            pool_recycle=3600,
            pool_size=20,
            max_overflow=20,
            pool_pre_ping=True
        )

    @staticmethod
    def __create_session(engine: Engine) -> scoped_session:
        return scoped_session(
            sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)
        )

    @contextmanager
    def session_scope(self) -> Session:
        session = self.__create_session(self.__engine)()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
        finally:
            session.close()

    @contextmanager
    def execute_query(self):
        yield self.__engine.execute


dao = DAO()

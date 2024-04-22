from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import db_url

engine = create_engine(db_url)
session_maker = sessionmaker(engine)


class Base(DeclarativeBase):
    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}" for col in self.__table__.columns.keys()]
        return f"<{self.__class__.__name__} {','.join(cols)}>"

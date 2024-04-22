from sqlalchemy import select, insert, delete

from app.database.db_connect import session_maker



class BaseRepo:
    model = None

    @classmethod
    def find_all(cls, **filter_by):
        with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = session.execute(query)
            return result.scalars().all()

    @classmethod
    def add(cls, **data):
        with session_maker() as session:
            query = insert(cls.model).values(data)
            session.execute(query)
            session.commit()

    @classmethod
    def find_by_id(cls, model_id: int):
        with session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    def delete_by_id(cls, model_id: int):
        with session_maker() as session:
            query = delete(cls.model).filter_by(id=model_id)
            session.execute(query)
            session.commit()

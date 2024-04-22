from sqlalchemy import select
from sqlalchemy.orm import aliased, joinedload, selectinload

from app.database.db_connect import session_maker
from app.database.repo import BaseRepo
from app.methodologies.models import Methodologies, ImagesInMethodologies
from app.methodologies.schemas import MethodologiesRelDTO


class MImagesRepo(BaseRepo):
    model = ImagesInMethodologies


class MethodologiesRepo(BaseRepo):
    model = Methodologies

    @classmethod
    def join_method_images(cls, model_id):
        with session_maker() as session:
            query = (
                select(Methodologies)
                .filter_by(id=model_id)
                .options(selectinload(Methodologies.images))
            )
            res = session.execute(query)
            result = res.scalars().all()
            return MethodologiesRelDTO.model_validate(*result, from_attributes=True)

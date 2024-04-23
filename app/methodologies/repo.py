from sqlalchemy import select

from app.database.db_connect import session_maker
from app.database.repo import BaseRepo
from app.methodologies.models import Methodologies, ImagesInMethodologies


class MImagesRepo(BaseRepo):
    model = ImagesInMethodologies

    @staticmethod
    def get_images_for_method(model_id):
        with session_maker() as session:
            query = select(ImagesInMethodologies.url).filter_by(method_id=model_id)
            return session.execute(query).scalars().all()


class MethodologiesRepo(BaseRepo):
    model = Methodologies



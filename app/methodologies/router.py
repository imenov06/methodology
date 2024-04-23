import time

from fastapi import APIRouter

from app.methodologies.utils import get_methodology_with_images, get_all_methodologies_with_images
from app.methodologies.schemas import SMethod
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/api/methodologies"
)


@router.get("/get/{model_id}")
@cache(expire=60)
def get_methodology_by_id(model_id: int) -> SMethod:
    schema_method = get_methodology_with_images(model_id)
    return schema_method


@router.get("/get")
@cache(expire=60)
def get_all_methodologies() -> list[SMethod]:
    list_schemas_methods = get_all_methodologies_with_images()
    return list_schemas_methods

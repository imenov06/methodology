from app.methodologies.repo import MethodologiesRepo, MImagesRepo
from app.methodologies.schemas import SMethod
from fastapi import HTTPException, status


def get_methodology_with_images(model_id: int) -> SMethod:
    method = MethodologiesRepo.find_by_id(model_id)
    images = MImagesRepo.get_images_for_method(model_id)
    if method is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Методология с id={model_id} не найдена."
                            )

    schema = SMethod(
        id=method.id,
        title=method.title,
        description=method.description,
        avatar_url=method.avatar_url,
        is_published=method.is_published,
        images=images
    )
    return schema


def get_all_methodologies_with_images() -> list[SMethod]:
    methods = MethodologiesRepo.find_all()
    list_methodologies = []

    for method in methods:
        images = MImagesRepo.get_images_for_method(method.id)
        schema = SMethod(
            id=method.id,
            title=method.title,
            description=method.description,
            avatar_url=method.avatar_url,
            is_published=method.is_published,
            images=images
        )
        list_methodologies.append(schema)
    return list_methodologies

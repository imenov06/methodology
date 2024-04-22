from pydantic import BaseModel


class MethodologiesAddDTO(BaseModel):
    title: str
    description: str
    avatar_url: str
    is_published: bool


class MethodologiesDTO(MethodologiesAddDTO):
    id: int


class ImagesAddDTO(BaseModel):
    url: str
    method_id: int


class ImagesDTO(ImagesAddDTO):
    id: int


class MethodologiesRelDTO(MethodologiesDTO):
    images: list['ImagesDTO']


class ImagesRelDTO(ImagesDTO):
    method: "MethodologiesDTO"

from pydantic import BaseModel


class SMethod(BaseModel):
    id: int
    title: str
    description: str
    avatar_url: str
    is_published: bool

    images: list[str]




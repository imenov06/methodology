from fastapi import APIRouter, Request, Depends
from starlette.templating import Jinja2Templates

from app.methodologies.router import get_all_methodologies
from app.methodologies.utils import get_methodology_with_images

view = APIRouter()
templates = Jinja2Templates(directory="app/pages/templates")


@view.get("/")
def show_main_page(
        request: Request,
        methodologies=Depends(get_all_methodologies)
):
    return templates.TemplateResponse(name='index.html', context={"request": request, "methodologies": methodologies})


@view.get("/{id}")
def show_method(request: Request,
                method=Depends(lambda id: get_methodology_with_images(id))
                ):
    return templates.TemplateResponse(name='product.html', context={"request": request, "methodology": method})

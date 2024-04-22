from fastapi import APIRouter

router = APIRouter(
    prefix="/methodologies"
)

@router.get("/get_all")
def get_all_methodologies():
    pass
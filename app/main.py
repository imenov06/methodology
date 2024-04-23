from fastapi import FastAPI
from app.database.core import Core
from app.methodologies.router import router as method_router

app = FastAPI()
app.include_router(method_router)


@app.on_event("startup")
def startup():
    Core.create_tables()
    Core.insert_test_data()

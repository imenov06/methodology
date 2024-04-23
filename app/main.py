from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.config import get_settings
from app.database.core import Core
from app.methodologies.router import router as method_router

from redis import asyncio as aioredis

app = FastAPI()
app.include_router(method_router)


@app.on_event("startup")
def startup():
    redis = aioredis.from_url(get_settings().get_redis_url(), decode_response=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")

    Core.create_tables()
    Core.insert_test_data()

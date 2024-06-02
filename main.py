from fastapi import FastAPI
from app.infrastructure.api.routers import route_newsletter

app = FastAPI()

app.include_router(
    route_newsletter.router, prefix="/newsletter", tags=["newsletter"])

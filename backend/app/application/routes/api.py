from fastapi import APIRouter

from application.core.api.db_api import router as db_router

api_router = APIRouter()
api_router.include_router(db_router)

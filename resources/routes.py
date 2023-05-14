from fastapi import APIRouter
from resources import user



api_router = APIRouter()


api_router.include_router(user.router)
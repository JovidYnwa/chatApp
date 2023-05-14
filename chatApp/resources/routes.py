from fastapi import APIRouter
from resources import user, sock

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(sock.sock_router)
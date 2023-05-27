from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from config.db import collection
from managers.user import UserExistsException, UserManager
from models.user import User
from schemas.response.user import UserOut


user_router = APIRouter()

@user_router.post("/users", response_model=UserOut)
async def create_user(request: Request, user: User):
    try:
        query = UserManager.create_user(user)
    except UserExistsException:
        raise HTTPException(status_code=409, detail="User already excists")
    return query


@user_router.get("/get_users")
async def get_user():
    user = list(collection["users"].find({"age":0}))
    return {"success": "Jaaaa"}
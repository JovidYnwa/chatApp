from typing import List
from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from managers.user import UserExistsException, UserManager
from models.user import User
from schemas.request.user import UserContactsIn
from schemas.response.user import UserOut


user_router = APIRouter(tags=["User"])

@user_router.post("/users", response_model=UserOut)
async def create_user(request: Request, user: User):
    try:
        query = UserManager.create_user(user)
    except UserExistsException:
        raise HTTPException(status_code=409, detail="User already exists")
    return query


@user_router.post("/user_contacts", response_model=List)
async def get_user_contacts(request: Request, users: UserContactsIn):
    """All contact that registrated in app
    """
    query = UserManager.get_existing_contacts(users)
    return query
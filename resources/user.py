from fastapi import APIRouter

from models.user import User
from config.db import collection


router = APIRouter()

@router.post("/users")
async def create_user(user: User):
    # Convert user object to dict
    user_data = user.dict()
    
    # Insert the user document into the collection
    result = collection.insert_one(user_data)
    
    return {"inserted_id": str(result.inserted_id)}
from fastapi import APIRouter

from models.user import User, Post
from config.db import collection


router = APIRouter()

@router.post("/users")
async def create_user(user: User):
    # Convert user object to dict
    users_collection = collection["users"]
    

    users_collection.insert_one(dict(user))
    return {"inserted_id": "yo"}


@router.post("/post")
async def create_user(post: Post):
    posts_collection = collection["posts"]

    posts_collection.insert_one(dict(post))
    
    return {"inserted_id": "yo"}


@router.get("/get_users")
async def get_user():
    # Convert user object to dict
    users_collection = collection["posts"]

    users = collection.find()
    user_instances = []
    for user_data in users:

        user_instances.append(user_data)
    print(user_instances, "fuck")

    
    return {"inserted_id": 1}
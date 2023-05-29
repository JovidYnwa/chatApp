from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId


class ChatRoomOut(BaseModel):
    id: str = Field(alias="_id")
    room_name: str
    description: str
    participants: List[str]  # List of user IDs



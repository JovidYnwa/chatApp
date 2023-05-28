from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class ChatRoom(BaseModel):
    creator_id: str
    room_name: str
    description: str
    participants: List[str]  # List of user IDs
    end_date: str



from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class ChatRoom(BaseModel):
    room_name: str
    description: str
    participants: List[str]  # List of user IDs
    start_date: str = Field(default_factory=lambda: datetime.now().strftime("%d.%m.%Y %H:%M"))
    end_date: str
    # Other chat room attributes
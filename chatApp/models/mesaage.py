from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    content: str
    sender: str  # User ID of the sender
    timestamp: str
    room_id: str  # ID of the chat room
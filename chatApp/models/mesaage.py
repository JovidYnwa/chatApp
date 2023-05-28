from pydantic import BaseModel
from datetime import datetime, validator


class Message(BaseModel):
    room_id: str  # ID of the chat room
    sender_id: str  # User ID of the sender
    content: str
    timestamp: str
    timestamp: datetime

    @validator('timestamp', pre=True, always=True)
    def set_timestamp(cls, value):
        return datetime.now().strftime('%d.%m.%Y %H:%M:%S')

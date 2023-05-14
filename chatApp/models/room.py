from pydantic import BaseModel
import uuid


class Room(BaseModel):
    room_id: str = str(uuid.uuid4())
    description: str

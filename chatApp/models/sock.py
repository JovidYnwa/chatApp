from ast import List
from pydantic import BaseModel
from fastapi import WebSocket



class UserSocket(BaseModel):
    socket_id: List[WebSocket]

    def __str__(self):
        return self.clint_id

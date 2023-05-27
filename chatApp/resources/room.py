from typing import List
from fastapi import APIRouter
from starlette.requests import Request
from managers.room import ChatRoomManager
from schemas.request.room import ChatRoom
from schemas.response.room import ChatRoomOut

room_router = APIRouter()

@room_router.post("/chatroom/")
async def create_chatroom(request: Request, chat_room: ChatRoom):
    return ChatRoomManager.create_room(chat_room)


@room_router.get("/chatroom/", response_model=List[ChatRoomOut])
async def get_chatroom():
    chat_rooms = ChatRoomManager.get_chatroom()
    converted_chat_rooms = [
        ChatRoomOut(**{**room, "_id": str(room["_id"])}) for room in chat_rooms
    ]
    return converted_chat_rooms
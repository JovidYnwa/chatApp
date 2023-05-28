from typing import List
from fastapi import APIRouter
from starlette.requests import Request
from managers.room import ChatRoomManager
from schemas.request.room import ChatRoom
from schemas.response.room import ChatRoomOut

room_router = APIRouter(tags=["Room"])

@room_router.post("/chatroom/")
async def create_chatroom(request: Request, chat_room: ChatRoom):
    return ChatRoomManager.create_room(chat_room)


@room_router.get("/chatroom/{room_id}", )
async def get_chatroom(room_id: str):

    chat_room = ChatRoomManager.get_chatroom(room_id)
    converted_chat_rooms = [
        ChatRoomOut(**{**room, "_id": str(room["_id"])}) for room in chat_room
    ]
    return converted_chat_rooms


@room_router.get("/chatrooms/", response_model=List[ChatRoomOut])
async def get_chatrooms():
    """Not for all users
    """
    chat_rooms = ChatRoomManager.get_chatroom()
    converted_chat_rooms = [
        ChatRoomOut(**{**room, "_id": str(room["_id"])}) for room in chat_rooms
    ]
    return converted_chat_rooms
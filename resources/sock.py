import json
from typing import Dict
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from config.db import collection
from managers.message import MessageManager
from managers.room import ChatRoomManager


sock_router = APIRouter()



# In-memory storage for active WebSocket connections (latter on shoud do though Redis)
active_connections: Dict[str, WebSocket] = {}

@sock_router.websocket("/ws/{user_id}")
async def websocket_endpoint(user_id: str, websocket: WebSocket):
    await websocket.accept()

    # Store WebSocket connection
    active_connections[user_id] = websocket

    try:
        while True:
            # Receive message (in json format) from WebSocket
            message_data = await websocket.receive_json()
            MessageManager.create_message(message_data)# Save the message to MongoDB


            #Send messages (Dont like this implemataion should figure smth else)
            room = ChatRoomManager.get_chatroom(message_data["room_id"])
            print("======> ", room)
            participants = room[0]["participants"]
            for participant in participants:
                try:
                    if participant != user_id:
                        print("(-----)", type(message_data))

                        await active_connections[participant].send_text((message_data)) #Seding message
                except:
                    pass

            # if recipient_websocket:
            #     # Send message to recipient
            #     await recipient_websocket.send_text(message_data)
            # else:
            #     # Handle recipient not online
            #     # You can choose to store the message for later delivery or handle it in any other way
            #     print(f"Recipient '{message_data.recipient}' is not online. Message could not be delivered.")
    except WebSocketDisconnect:
        del active_connections[user_id]# Remove WebSocket connection

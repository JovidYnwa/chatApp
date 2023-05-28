from typing import Dict
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from config.db import collection


sock_router = APIRouter()



# In-memory storage for active WebSocket connections (latter on shoud do though Redis)
active_connections: Dict[str, WebSocket] = {}


@sock_router.websocket("/ws/{user_id}")
async def websocket_endpoint(user_id: str, websocket: WebSocket):
    await websocket.accept()
    socket_collection = collection["usersockets"]

    # Store WebSocket connection
    active_connections[user_id] = websocket
    
    try:
        while True:
            # Receive message from WebSocket
            message_data = await websocket.receive_text()
            print("message data equeals to = ", message_data)
            # Save the message to MongoDB

            # Get recipient's WebSocket
            recipient_websocket = active_connections.get(message_data.recipient)
            if recipient_websocket:
                # Send message to recipient
                await recipient_websocket.send_text(message_data)
            else:
                # Handle recipient not online
                # You can choose to store the message for later delivery or handle it in any other way
                print(f"Recipient '{message_data.recipient}' is not online. Message could not be delivered.")
    except WebSocketDisconnect:
        del active_connections[user_id]# Remove WebSocket connection




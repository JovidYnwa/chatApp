from typing import Dict
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from config.db import collection


sock_router = APIRouter()



# In-memory storage for active WebSocket connections
active_connections: Dict[str, WebSocket] = {}


@sock_router.websocket("/ws/{user_id}")
async def websocket_endpoint(user_id: str, websocket: WebSocket):
    await websocket.accept()
    socket_collection = collection["usersockets"]

    # Store WebSocket connection
    active_connections[user_id] = websocket
    print("===> ", active_connections)
    pass
    try:
        while True:
            # Receive message from WebSocket
            message_data = await websocket.receive_text()
            #message = Message.parse_raw(message_data)

            # Save the message to MongoDB
            #socket_collection.insert_one(message.dict())

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
        # Remove WebSocket connection
        del active_connections[user_id]


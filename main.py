from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
from resources.routes import api_router
from config.db import collection


app = FastAPI()
app.include_router(api_router)

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(user_id: str, websocket: WebSocket):
    await websocket.accept()

    # Store the WebSocket connection in MongoDB
    connection_data = {"user_id": user_id, "websocket": websocket.scope["client"]}
    collection.insert_one(connection_data)

    try:
        while True:
            message = await websocket.receive_text()
            # Process incoming messages from the WebSocket connection
            print(f"Received message from {user_id}: {message}")
    except WebSocketDisconnect:
        # Remove WebSocket connection from MongoDB
        collection.delete_one({"user_id": user_id})
        # Handle WebSocket disconnection
        print(f"WebSocket disconnected: {user_id}")




if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
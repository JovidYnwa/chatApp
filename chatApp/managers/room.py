from config.db import collection
from bson import ObjectId


class ChatRoomManager:
    
    @staticmethod
    def get_chatroom(chatroom_data=None):
        room_collection = collection["chat_room"]

        if chatroom_data is not None:
            query = {"_id": ObjectId(chatroom_data)}
        else:
            query={}
            
        chat_rooms =  room_collection.find(query)
        print("======> ",chat_rooms)
        return [room for room in chat_rooms]

    
    @staticmethod
    def create_room(chatroom_data):
        room_collection = collection["chat_room"]
        result = room_collection.insert_one(dict(chatroom_data))
        room_id = str(result.inserted_id)

        #also creating new instance with id on redis
        #active_connections
        return room_id

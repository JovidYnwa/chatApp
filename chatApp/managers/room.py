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
        return [room for room in chat_rooms]

    
    @staticmethod
    def create_room(chatroom_data):
        room_collection = collection["chat_room"]
        chatroom_data.participants.append(chatroom_data.creator_id) #Inserting creator of to the paricipants
        result = room_collection.insert_one(dict(chatroom_data))
        room_id = str(result.inserted_id)
        return room_id

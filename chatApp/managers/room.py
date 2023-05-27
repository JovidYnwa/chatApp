from config.db import collection


class ChatRoomManager:
    
    @staticmethod
    def get_chatroom():
        room_collection = collection["chat_room"]
        chat_rooms =  room_collection.find()
        return [room for room in chat_rooms]

    
    @staticmethod
    def create_room(chatroom_data):
        room_collection = collection["chat_room"]
        result = room_collection.insert_one(dict(chatroom_data))
        room_id = str(result.inserted_id)
        return room_id

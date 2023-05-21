from config.db import collection

import asyncio



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
    
    # @staticmethod
    # async def delete_complaint(complaint_id):
    #     await database.execute(complaint.delete().where(complaint.c.id == complaint_id))

    # @staticmethod
    # async def approve(id_):
    #     await database.execute(complaint.update().where(complaint.c.id == id_).values(status=State.approver))

    # @staticmethod
    # async def reject(id_):
    #     await database.execute(complaint.update().where(complaint.c.id == id_).values(status=State.rejected))
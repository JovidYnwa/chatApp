from config.db import collection

class UserExistsException(Exception):
    pass

class UserManager:
    
    # @staticmethod
    # def get_chatroom():
    #     room_collection = collection["chat_room"]
    #     chat_rooms =  room_collection.find()
    #     return [room for room in chat_rooms]

    
    @staticmethod
    def create_user(user_data):
        user_collection = collection["user"]
        existing_user = user_collection.find_one({"msisdn": user_data.msisdn})

        if existing_user:
            raise UserExistsException("User already exists")

        result = user_collection.insert_one(dict(user_data))
        inserted_id = result.inserted_id
        inserted_document = user_collection.find_one({"_id": inserted_id})
        return inserted_document

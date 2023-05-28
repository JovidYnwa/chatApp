import json
from config.db import collection




class MessageManager:
    
    # @staticmethod
    # def get_existing_contacts(user_data):
    #     user_collection = collection["message"]
    #     serialized_data = json.loads(user_data.json())
    #     query = {"msisdn": {"$in": serialized_data['msisdns']}}
    #     result = user_collection.find(query)
    #     existing_contacts = [contact["msisdn"] for contact in result]
    #     return existing_contacts

    
    @staticmethod
    def create_message(user_data):
        user_collection = collection["message"]
        result = user_collection.insert_one(user_data)
        inserted_id = result.inserted_id
        inserted_document = user_collection.find_one({"_id": inserted_id})
        return inserted_document
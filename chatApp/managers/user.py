import json
from config.db import collection

class UserExistsException(Exception):
    pass


class UserManager:
    
    @staticmethod
    def get_existing_contacts(user_data):
        user_collection = collection["user"]
        serialized_data = json.loads(user_data.json())
        query = {"msisdn": {"$in": serialized_data['msisdns']}}
        result = user_collection.find(query)
        existing_contacts = [contact["msisdn"] for contact in result]
        return existing_contacts

    
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

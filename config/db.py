from pymongo import MongoClient


DATABASE_URL = "mongodb://localhost:27017/mychat"

# Connect to MongoDB using the DATABASE_URL
client = MongoClient(DATABASE_URL)

# Access the desired database
database = client.get_database()

# Access a collection within the database
collection = database["collection_chat"]

# Perform operations on the collectionth
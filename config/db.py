from pymongo import MongoClient


DATABASE_URL = "mongodb://localhost:27017/test"

# Connect to MongoDB using the DATABASE_URL
client = MongoClient(DATABASE_URL)

# Access the desired database
database = client.get_database()

# Access a collection within the database
collection = database["collection_name"]

# Perform operations on the collection
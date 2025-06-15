from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client.get_default_database()

# Define collections
customer_collection = db["customer_collection"]
properties_collection = db["properties_collection"]
users_collection = db["users"]

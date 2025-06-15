from pymongo import MongoClient
import os
import certifi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the connection string from environment variable
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas with proper TLS certificate
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())

# Access your database (replace with your actual DB name if needed)
db = client.get_database()

# Define collections
customer_collection = db["customer_collection"]
properties_collection = db["properties_collection"]
users_collection = db["users"]

import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from a .env file (only needed for local dev)
load_dotenv()

# Get the Mongo URI from environment variable
MONGO_URI = os.environ.get("MONGO_URI")

# Create Mongo client with TLS and CA file
client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where()
)

# Select database
db = client.realestate_db

# Define collections
customer_collection = db["customer_collection"]
properties_collection = db["properties_collection"]
users_collection = db["users"]

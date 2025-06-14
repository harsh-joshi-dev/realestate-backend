from pymongo import MongoClient

client = MongoClient("mongodb+srv://kellyharrisoninfo:1gNy7ZxN8VoQHDE9@project0.e1kmvyv.mongodb.net/?retryWrites=true&w=majority&appName=Project0")

# Use one database
db = client.realestate_db

# Define multiple collections
customer_collection = db["customer_collection"]
properties_collection = db["properties_collection"]
users_collection = db["users"]

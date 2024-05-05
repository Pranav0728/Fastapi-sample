import os

from pymongo import MongoClient

from dotenv import load_dotenv
load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL")

# Connect to MongoDB

client = MongoClient(MONGODB_URL)
db = client.my_database  
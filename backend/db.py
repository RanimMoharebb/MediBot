import dns.resolver
# Force this script to look up MongoDB via Google's DNS without touching your PC network settings
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '1.1.1.1']

from pymongo import MongoClient
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# ✅ MongoDB connection string (must be a string)
MONGO_URI = "mongodb+srv://ranimmohareb650_db_user:J6jav3mKU7SVDY1o@cluster0.gvt1vlu.mongodb.net/"

# ✅ Connect to MongoDB
client = MongoClient(MONGO_URI)

# ✅ Use database "medical_chatbot"
db = client["medical_chatbot"]

# ✅ Use collection "chats"
chat_collection = db["chats"]
user_collection = db["users"]  # NEW

# ✅ Save a single chat record
def save_chat(username, prompt, response):
    chat_doc = {
        "username": username,
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.now().isoformat()
    }
    chat_collection.insert_one(chat_doc)

# ✅ Get all chat history for a user
def get_chat_history(username):
    return list(chat_collection.find({"username": username}))

def clear_chat_history(username):
    if username:
        chat_collection.delete_many({"username": username})

# NEW: Register user
def create_user(name, email, password, dob, gender):
    if user_collection.find_one({"email": email}):
        return False, "User already exists"
    hashed = generate_password_hash(password)
    user = {
        "name": name,
        "email": email,
        "password": hashed,
        "dob": dob,
        "gender": gender
    }
    user_collection.insert_one(user)
    return True, user

# NEW: Login user
def authenticate_user(email, password):
    user = user_collection.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return False, "Invalid credentials"
    return True, user
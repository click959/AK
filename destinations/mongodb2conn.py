from pymongo import MongoClient

client = MongoClient("mongodb+srv://AK:okay@cluster0.smdfz.mongodb.net/HotelDestinationPage?retryWrites=true&w=majority")
db = client.get_database("HotelDestinationPage")
collection = db.full_hotels

def fetch_one(id):
    if collection is None:
        return None
    else:
        alldestinations = collection.find_one({"id" : id})
        return alldestinations


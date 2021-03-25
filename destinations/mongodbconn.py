from pymongo import MongoClient

client = MongoClient("mongodb+srv://AK:okay@cluster0.smdfz.mongodb.net/HotelDestinationPage?retryWrites=true&w=majority")
db = client.hotels

def fetchData():
    if db is None:
        return None
    else:
        print(db.find())
        
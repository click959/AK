from pymongo import MongoClient

db = None
def createconnection():
    client = MongoClient("mongodb+srv://AK:okay@cluster0.smdfz.mongodb.net/HotelDestinationPage?retryWrites=true&w=majority")
    db = client.hotels

def fetchData():
    createconnection()
    if db is None:
        return None
    else:
        print(db)
        
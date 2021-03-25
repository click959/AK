from pymongo import MongoClient

db = None
def createconnection():
    client = MongoClient("mongodb+srv://AK:okay@cluster0.smdfz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test

def fetchData():
    if db is None:
        return None
    else:
        print("hello")
        
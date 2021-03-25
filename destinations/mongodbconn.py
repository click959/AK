from pymongo import MongoClient

client = MongoClient("mongodb+srv://AK:<password>@cluster0.smdfz.mongodb.net/HotelDestinationPage?retryWrites=true&w=majority")
db = client.hotels
print(db.count_documents({}))
print("running")
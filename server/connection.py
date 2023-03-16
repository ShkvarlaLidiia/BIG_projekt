from pymongo import MongoClient

def connection():
    CONNECTION_STRING = "mongodb+srv://sly1712:4444@cluster0.t3hcym5.mongodb.net/?retryWrites=true&w=majority"   
    client = MongoClient(CONNECTION_STRING)
    return client['DBdb']

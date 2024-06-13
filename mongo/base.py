#!/usr/bin/python3

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class Storage:
    def __init__(self, uri, database, coll):
        self.client = MongoClient(uri)
        try:
            self.client.admin.command('ping')
            print("Conectado a MongoDB")
        except ConnectionFailure:
            print("Server not available")
            raise
        self.db = self.client[database]
        self.collection = self.db[coll]

    def update(self, Id, value):
        result = self.collection.update_many({'_id': Id}, {'$set': value}, upsert=True)
        return result

    def find(self):
        return list(self.collection.find())

    def find_one(self, query):
        return self.collection.find_one(query)

if __name__ == "__main__":
    uri = "mongodb://localhost:27017/"
    database = ""
    coll = ""

    storage = Storage(uri, database, coll)
    


from pymongo import MongoClient

class Collection:
    dbName = "organizzer"
    host = "localhost"
    port = 27017

    client = MongoClient(host, port)
    db = client[dbName]

    def __init__(self, collectionName):
        self.collection = collectionName

    def find(self):
        return self.db[self.collection].find_one()

    def insert(self, data):
        """ this string is a description of this method. For example """
        
        self.db[self.collection].insert_one(data)


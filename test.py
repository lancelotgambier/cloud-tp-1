from pymongo import MongoClient

CONNECTION_STRING = # Your connection string
client = MongoClient(CONNECTION_STRING)
db = client['mongo1']
collection = db['collection1']

# Test query
documents = collection.find()
for doc in documents:
    print(doc)

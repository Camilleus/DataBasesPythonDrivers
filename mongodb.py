from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://magnetonbohra:I7RL0iG8DxTNXVJi@cluster0.wellc9q.mongodb.net/"
)

sample_guides_db = client.get_database("sample_guides")

print("Collections: ")
for collection in sample_guides_db.list_collection_names():
    print(collection)

planets_collectin = sample_guides_db.get_collection("planets")

print("Documents: ")
for doc in planets_collectin.find():
    print(doc)
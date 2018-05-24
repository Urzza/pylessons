from classes.db_class import Collection

collection = Collection("users")

print(collection.find())

collection.insert({"name":"Arnold", "age":33, "counry":"Argentina"})

print(collection.find())

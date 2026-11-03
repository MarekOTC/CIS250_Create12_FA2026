# Import Module
from pymongo import MongoClient
import json
 
# Create a MongoClient object on port 27017
client = MongoClient('mongodb://localhost:27017')

# Connect to a database
db = client['school']

# Specify collection
collection = db['student']

# Use find_one to return one document
result = collection.find_one()

# # Ugly Print
# print(result)

# # Pretty Print
# print(json.dumps(result, indent=4, default=str))

# # Use find() to display all documents
# result = collection.find()

# # Loop through result to print each document
# for document in result:
#     print(json.dumps(document,indent=4,default=str))

# Use find() with criteria to search for documents
result = collection.find({'gpa':3.5})

for document in result:
    print(json.dumps(document,indent=4,default=str))


"""Utility script to ensure a default Site document exists in MongoDB.
This bypasses Django ORM issues with djongo during post_migrate.
"""
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['octofit_db']
collection = db['django_site']

# Check for _id=1 and create if missing
if collection.count_documents({'_id': 1}) == 0:
    collection.insert_one({'_id': 1, 'domain': 'localhost:8000', 'name': 'localhost'})
    print('Inserted default Site document')
else:
    print('Default Site document already exists')

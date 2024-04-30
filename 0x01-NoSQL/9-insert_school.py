#!/usr/bin/env python3
"task 9 module"


def insert_school(mongo_collection, **kwargs):
    "inserts new document"
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

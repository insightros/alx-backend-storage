#!/usr/bin/env python3
"task 10 module"


def update_topics(mongo_collection, name, topics):
    "changes topics"
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

#!/usr/bin/env python3
"task 11 module"


def schools_by_topic(mongo_collection, topic):
    "returns the list of schools"
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]

#!/usr/bin/env python3
"""filter topic"""


def schools_by_topic(mongo_collection, topic: str):
    """return result based on topic
    params:
        collection name, topic for search
    return:
        list of schools with topic
    """
    data = mongo_collection.find({"topics": topic})
    return data

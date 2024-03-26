#!/usr/bin/env python3
"""updating data"""


def update_topics(mongo_collection, name, topics):
    """update topic based on name
        params:
            collection, name for search
            and topics to add
        return:
            None
    """
    data = mongo_collection.update_one(
        {"name": name}, {"$set": {"topics": topics}}
        )   # take query and data
    return data.upserted_id

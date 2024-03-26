#!/usr/bin/env python3
"""sorting data"""


def top_students(mongo_collection):
    """sorts data by average score
    params:
        mongo collection
    return:
        ordered list
    """
    # data = mongo_collection.aggregate([
    #     {"$addFields": {
    #         "averageScore": {"$avg": "$topics.score"}
    #     }},
    #     {"$sort": {
    #         "averageScore": -1
    #     }},
    #     {"$project": {
    #         "_id": 1,
    #         "name": 1,
    #         "averageScore": 1
    #     }}
    # ])
    pipeline = [
        {"$addFields": {"averageScore": {"$avg": "$scores"}}},  # Calculate average score
        {"$sort": {"averageScore": -1}},  # Sort by average score in descending order
        {"$project": {"_id": 1, "name": 1, "averageScore": 1}}  # Project only required fields
    ]
    top_student = list(mongo_collection.aggregate(pipeline))
    return top_student

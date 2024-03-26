#!/usr/bin/env python3
"""sorting data"""
from typing import List


def top_students(mongo_collection) -> List:
    """sorts data by average score"""
    pipeline = [
        {"$addFields": {"averageScore": {"$avg": "$scores"}}},
        {"$sort": {"averageScore": -1}}
    ]
    top_students = list(mongo_collection.aggregate(pipeline))
    return top_students

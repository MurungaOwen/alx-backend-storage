#!/usr/bin/env python3
"""sorting data"""
from typing import List


def top_students(mongo_collection) -> List:
    """sorts data by average score"""
    """
    db.students.aggregate([
        {$addFields: 
            {averageScore: { $avg: "$topics.score" }}
        }, 
        {$group: 
            {_id: "$name", averageScore: { $first: "$averageScore" } }
        },
        {$sort: { averageScore: -1 }}
    ]);
    """
    pass

#!/usr/bin/env python3

""" Module for using PyMongo """


if __name__ == '__main__':
    def top_students(mongo_collection):
        """ Returns all students sorted by average score"""
        top_student = mongo_collection.aggregate([
            {
                "$project": {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
            },
            {"$sort": {"averageScore": -1}}
        ])

        return top_student
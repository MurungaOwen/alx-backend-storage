#!/usr/bin/env python3
"""contains function to list docs"""
from typing import List


def list_all(mongo_collection) -> List:
    """a script to list objects in collect
    ion
    params:
        mongo_collection as collection
    return:
        list of documents
    """
    result = mongo_collection.find()
    return result

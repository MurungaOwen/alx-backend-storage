#!/usr/bin/env python3
"""script to insert documents in 
collection
"""
from typing import Any


def insert_school(mongo_collection, **kwargs) -> Any:
    """insert data to collection
    params:
        take in collection and data
    return:
        inserted id
    """
    add_data = {}
    for key, value in kwargs.items():
        add_data[key] = value
    
    data = mongo_collection.insert_one(add_data)
    return data.inserted_id

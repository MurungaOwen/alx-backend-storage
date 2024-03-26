#!/usr/bin/env python3
"""nginx logs"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all


client = MongoClient('mongodb://127.0.0.1:27017')
db = client["logs"]
collection = db.get_collection("nginx")


def get_total() -> int:
    """return total contents"""
    return collection.count_documents({})


def methods_total() -> int:
    """return total /status"""
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods: ")
    for x in method:
        total = collection.count_documents({"method": x})
        print(f'    method {x}: {total}')
    return f'{collection.count_documents({"path": "/status"})} status check'


print(f'{get_total()} logs')
print(methods_total())

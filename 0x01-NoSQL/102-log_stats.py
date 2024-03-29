#!/usr/bin/env python3
"""upgrade of 12-log_stats by adding the top 10 most present ips"""
from pymongo import MongoClient


if __name__ == '__main__':
    METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    PIPE = [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}, {"$limit": 10}]

    def log_stats(mongo_collection, option=None):
        """
        Prototype: def log_stats(mongo_collection, option=None):
        Provide some stats about Nginx logs stored in MongoDB
        """
        items = {}
        if option:
            value = mongo_collection.count_documents(
                {"method": {"$regex": option}})
            print(f"\tmethod {option}: {value}")
            return

        result = mongo_collection.count_documents(items)
        print(f"{result} logs")
        print("Methods:")
        for method in METHODS:
            log_stats(nginx_collection, method)
        status_check = mongo_collection.count_documents({"path": "/status"})
        print(f"{status_check} status check")
        print("IPs:")

        for ip in mongo_collection.aggregate(PIPE):
            print(f"\t{ip.get('_id')}: {ip.get('count')}")

    if __name__ == "__main__":
        nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
        log_stats(nginx_collection)

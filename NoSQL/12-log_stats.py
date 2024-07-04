#!/usr/bin/env python3
"""python scripts"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection, option=None):
    """ script that provides some stats about Nginx logs stored in MongoDB """
    if option:
        value = mongo_collection.count_documents({"method": option})
        print(f"\tmethod {option}: {value}")
        return

    # Total count of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count for each HTTP method
    print("Methods:")
    for method in METHODS:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Status check count
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    try:
        # Attempt to connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        print("Connected to MongoDB successfully")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        exit(1)

    # Access the collection
    try:
        db = client.logs
        nginx_collection = db.nginx
        print("Accessed nginx collection successfully")

        # Debug: Print a sample document
        sample_document = nginx_collection.find_one()
        if sample_document:
            print("Sample document from nginx collection:", sample_document)
        else:
            print("No documents found in the nginx collection")
    except Exception as e:
        print(f"Failed to access nginx collection: {e}")
        exit(1)

    # Perform logging statistics
    try:
        log_stats(nginx_collection)
    except Exception as e:
        print(f"An error occurred while fetching stats: {e}")
        exit(1)

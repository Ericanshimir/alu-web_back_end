#!/usr/bin/env python3
"""python scripts"""
import logging
from pymongo import MongoClient

# Configure logging
logging.basicConfig(filename='nginx_log_stats.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection, option=None):
    """ script that provides some stats about Nginx logs stored in MongoDB """
    if option:
        value = mongo_collection.count_documents({"method": option})
        logging.info(f"\tmethod {option}: {value}")
        print(f"\tmethod {option}: {value}")
        return

    # Total count of logs
    total_logs = mongo_collection.count_documents({})
    logging.info(f"{total_logs} logs")
    print(f"{total_logs} logs")

    # Count for each HTTP method
    logging.info("Methods:")
    print("Methods:")
    for method in METHODS:
        method_count = mongo_collection.count_documents({"method": method})
        logging.info(f"\tmethod {method}: {method_count}")
        print(f"\tmethod {method}: {method_count}")

    # Status check count
    status_check = mongo_collection.count_documents({"path": "/status"})
    logging.info(f"{status_check} status check")
    print(f"{status_check} status check")

if __name__ == "__main__":
    try:
        # Attempt to connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        logging.info("Connected to MongoDB successfully")
        print("Connected to MongoDB successfully")
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        print(f"Failed to connect to MongoDB: {e}")
        exit(1)

    # Access the collection
    try:
        db = client.logs
        nginx_collection = db.nginx
        logging.info("Accessed nginx collection successfully")
        print("Accessed nginx collection successfully")

        # Debug: Print a sample document
        sample_document = nginx_collection.find_one()
        if sample_document:
            logging.info(f"Sample document from nginx collection: {sample_document}")
            print(f"Sample document from nginx collection: {sample_document}")
        else:
            logging.info("No documents found in the nginx collection"
            print("No documents found in the nginx collection")
    except Exception as e:
        logging.error(f"Failed to access nginx collection: {e}")
        print(f"Failed to access nginx collection: {e}")
        exit(1)

    # Perform logging statistics
    try:
        log_stats(nginx_collection)
    except Exception as e:
        logging.error(f"An error occurred while fetching stats: {e}")
        print(f"An error occurred while fetching stats: {e}")
        exit(1)

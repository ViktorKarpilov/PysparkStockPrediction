from pymongo import MongoClient


mongo_client = MongoClient("mongodb+srv://bidatius:kRVWSMsJXlhyyW3C@appcluster.gbizgwf.mongodb.net/ohlc")
db = mongo_client["ohlc"]
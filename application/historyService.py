from flask_pymongo import PyMongo
from pymongo import MongoClient

class HistoryService:
    def __init__(self):
        self.mongo = MongoClient("mongodb+srv://bidatius:kRVWSMsJXlhyyW3C@appcluster.gbizgwf.mongodb.net/ohlc")
        self.db = self.mongo["ohlc"]

    def get_history(self, symbol, hours):
        cursor = self.db.appl_data.find({},{"_id":0}).limit(hours)
        result = [doc for doc in cursor]
        return result

historyService = HistoryService()


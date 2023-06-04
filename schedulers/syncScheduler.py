from flask_pymongo import PyMongo
from apscheduler.schedulers.background import BackgroundScheduler
from yahooquery import Ticker

class SyncScheduler:
    def __init__(self, app):
        self.mongo = PyMongo(app)
        self.db = self.mongo.db
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.trigger, 'interval', hours=1)
        self.scheduler.start()
    
    def trigger(self):
        print("[INFO]: Scheduler start !")
        ticker = Ticker("AAPL")
        data = ticker.history(period='30d', interval='1h')
        print(data.head())
        self.db.appl_data.delete_many({})
        self.db.appl_data.insert_many(data.reset_index().to_dict("records"))

syncScheduler = SyncScheduler
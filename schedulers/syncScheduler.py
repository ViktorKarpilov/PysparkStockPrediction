from apscheduler.schedulers.background import BackgroundScheduler
from yahooquery import Ticker

from db import db
from tqdm import tqdm


class SyncScheduler:
    def __init__(self, app):
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.trigger, 'interval', hours=1)
        self.scheduler.start()
    
    def trigger(self):
        print("[INFO]: Scheduler start !")
        pbar = tqdm(desc='Update', total=db.tickers.count_documents({}))
        for ticker_doc in db.tickers.find({}):
            symbol = ticker_doc['symbol']
            ticker = Ticker(symbol)
            data = ticker.history(period='30d', interval='1h').reset_index().to_dict("records")
            if db.ohlc.find_one({'symbol': symbol}, {'ohlc': 0}):
                db.ohlc.update_one(
                    {'symbol': symbol},
                    {'$set': {'ohlc': data}}
                )
            else:
                db.ohlc.insert_one({
                    'symbol': symbol,
                    'ohlc': data
                })
            pbar.update(1)

syncScheduler = SyncScheduler
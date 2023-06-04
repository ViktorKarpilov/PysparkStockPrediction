from db import db


class HistoryService:

    def get_history(self, symbol, hours):
        ticker = db.ohlc.find_one({'symbol': symbol}, {"_id": 0})
        ohlc = ticker['ohlc']
        return ohlc[len(ohlc) - hours:]

historyService = HistoryService()


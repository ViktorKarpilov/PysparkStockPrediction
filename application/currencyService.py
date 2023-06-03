from model.model_executor import model_executor
from yahooquery import Ticker
from datetime import datetime, timedelta

class CurrencyService():
    def __init__(this):
        this.__executor = model_executor

    def get_prediction(this, ticker, hours):
        ticker = Ticker(ticker, asynchronous=True)

        details = ticker.history(period='1h', interval='1h')
        target = details.tail(1)
        date = target.index[0][1]

        predict_y = this.__executor.predict(target["open"].values[0],
                                            target["high"].values[0],
                                            target["low"].values[0],
                                            target["close"].values[0],
                                            hours)
        result = []
        for y in predict_y:
            date += timedelta(hours=1)
            result.append([y, date])

        return result

currency_service = CurrencyService()
        

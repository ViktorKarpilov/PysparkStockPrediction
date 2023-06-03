from model.model_executor import model_executor
from yahooquery import Ticker

class CurrencyService():
    def __init__(this):
        __executor = model_executor

    def get_prediction(this, ticker, period):
        aapl = Ticker(ticker)

        # Summary Information
        details = aapl.summary_detail[ticker]
        traget = [(details["open"], details["dayHigh"], details["dayLow"], details["ask"], details["volume"])]
        __executor.predict(traget)

        return __executor.predict(traget, period)

currency_service = CurrencyService()
        

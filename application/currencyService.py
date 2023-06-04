from model.model_executor import model_executor
from yahooquery import Ticker
from datetime import datetime, timedelta
import json

class CurrencyService():
    def __init__(this):
        this.__executor = model_executor

    def get_prediction(this, ticker, hours):
        ticker = Ticker(ticker, asynchronous=True)

        details = ticker.history(period='3d', interval='1h')
        details = ticker.history(period='3d', interval='1h')
        target = details.tail(25)
        date = target.index[0][1]
        new_data = {}
        dickt_target = target.to_dict()
        target_data = {
            'DateTime': [],
            'Open': [],
            'High': [],
            'Low': [],
            'Close': [],
            'Volume': [],
        }

        for key, nested_dict in dickt_target.items():
            for tuple_key, value in nested_dict.items():
                ticker, timestamp = tuple_key
                target_data[key.capitalize()].append(value)  # Capitalize key for proper formatting
                if key == 'open':  # Append datetime only once
                    target_data['DateTime'].append(timestamp)

        predict_y = this.__executor.predict(target_data, hours)

        result = []
        for y in predict_y:
            date += timedelta(hours=1)
            result.append([y, date])

        return json.dumps(result)

currency_service = CurrencyService()
        

from model.model_executor import model_executor
from yahooquery import Ticker
from datetime import datetime, timedelta
import json

class CurrencyService():
    def __init__(this):
        this.__executor = model_executor

    def get_prediction(this, symbol, hours):
        ticker = Ticker(symbol, asynchronous=True)

        details = ticker.history(period='2w', interval='1h')
        target = details.tail(25)
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

        result = {
            'data': {
                'ticker': symbol,
                'candlestick': [],
                'prediction': []
            },
            'status': 'success', 'message': 'OK'
        }
        
        for i in range(len(target_data['DateTime'])):
            result['data']['candlestick'].append({
                'x': target_data['DateTime'][i].timestamp(),
                'y': [target_data['Open'][i], target_data['High'][i], target_data['Low'][i], target_data['Close'][i]]
            })

        latest_date = target.index[-1][1]
        for i, y in enumerate(predict_y, start=1):
            result['data']['prediction'].append({
                'x': (latest_date + timedelta(hours=i)).timestamp(),
                'y': y
            })

        return json.dumps(result)

currency_service = CurrencyService()
        

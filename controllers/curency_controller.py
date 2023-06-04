from flask import Blueprint
from flask.views import MethodView
from application.currencyService import currency_service

class CurrencyController(MethodView):
    def get(self, symbol, hours):
        # {
        #     "data": {
        #         "ticker": "ticker_name",
        #         "candlestick" : [
        #       {
        #          "x": 1685787016, // time
        #           "y" [open, high, low, close]
        #        },
        #        {
        #          "x": 1685787016, // time
        #           "y" [open, high, low, close]
        #        },
        #      .......
        #     ],
        #     "prediction": [
        #         {
        #            "x": 1234564 // time
        #            "y": 3234 // value
        #         },
        #           .......
        #     ]
        #     },
        #     "status": "success" / "error",
        #     "message": "error_message"
        # }
        return currency_service.get_prediction(symbol, int(hours))


currency_controller_bp = Blueprint('currency_controller', __name__)
currency_view = CurrencyController.as_view('currency_view')
currency_controller_bp.add_url_rule('/predict/<symbol>/<hours>', view_func=currency_view, methods=['GET'])
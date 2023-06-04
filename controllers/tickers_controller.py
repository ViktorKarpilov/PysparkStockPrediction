from flask import Blueprint
from flask.views import MethodView
from application.currencyService import currency_service
import json

from db import db

class TickersController(MethodView):
    def get(self):
        tickers = db.tickers.find({}, {'_id': 0})
        return json.dumps(list(tickers))


tickers_controller_bp = Blueprint('tickers_controller', __name__)
ticker_view = TickersController.as_view('tickers_view')
tickers_controller_bp.add_url_rule('/tickers', view_func=ticker_view, methods=['GET'])
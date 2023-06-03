from flask import Blueprint
from flask.views import MethodView
from application.currencyService import currency_service

class CurrencyController(MethodView):
    def get_prediction(self):
        return currency_service.get_prediction("aapl", 2)


currency_controller_bp = Blueprint('currency_controller', __name__)
currency_view = CurrencyController.as_view('currency_view')
currency_controller_bp.add_url_rule('/new_route', view_func=currency_view)
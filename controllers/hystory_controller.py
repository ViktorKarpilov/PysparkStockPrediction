from flask import Blueprint
from flask.views import MethodView
from application.historyService import  historyService
from flask import jsonify

import json

class HistoryController(MethodView):
    def get(self, symbol, hours):
        result = historyService.get_history(symbol, int(hours))
        return jsonify(result)

history_controller_bp = Blueprint('history_controller', __name__)
history_view = HistoryController.as_view('history_view')
history_controller_bp.add_url_rule('/history/<symbol>/<hours>', view_func=history_view, methods=['GET'])
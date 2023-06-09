from flask import Flask
from controllers.curency_controller import currency_controller_bp
from controllers.tickers_controller import tickers_controller_bp
from controllers.hystory_controller import history_controller_bp

class ControllerRegister():
    def include_controllers(this, app):
        app.register_blueprint(currency_controller_bp)
        app.register_blueprint(tickers_controller_bp)
        app.register_blueprint(history_controller_bp)

controllers_register = ControllerRegister()
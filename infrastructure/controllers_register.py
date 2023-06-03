from flask import Flask
from controllers.curency_controller import currency_controller_bp

class ControllerRegister():
    def include_controllers(this, app):
        app.register_blueprint(currency_controller_bp)

controllers_register = ControllerRegister()
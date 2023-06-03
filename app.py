from flask import Flask
from flask.views import MethodView
from infrastructure.controllers_register import controllers_register

app = Flask(__name__)
controllers_register.include_controllers(app)

class HelloWorld(MethodView):
    def get(self):
        return 'Hello, World!'

hello_world_view = HelloWorld.as_view('hello_world_view')
app.add_url_rule('/', view_func=hello_world_view)

if __name__ == '__main__':
    app.run(debug=True)
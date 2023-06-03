from flask import Flask
from flask.views import MethodView
from infrastructure.controllers_register import controllers_register

app = Flask(__name__)
controllers_register.include_controllers(app)

class Main(MethodView):

    def get(self):

        return 'Healthy!'

main_view = Main.as_view('main_view')
app.add_url_rule('/', view_func=main_view)

if __name__ == '__main__':
    # app.run(host='0.0.0.0')

    app.run(debug=True)
from flask import Flask
from flask_restful import Resource, Api

from resources.menu import Menu
from resources.order import Order

app = Flask(__name__)
api = Api(app)

api.add_resource(Menu, "/menu")

api.add_resource(Order, "/order")

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask
from flask_restful import Resource, Api

from resources.menu import Menu
from resources.order import Order
from resources.inventory import Inventory
from resources.ingridients import Ingridients

app = Flask(__name__)
api = Api(app)

api.add_resource(Menu, "/menu")

api.add_resource(Order, "/order")

api.add_resource(Inventory, "/inventory")

api.add_resource(Ingridients, "/ingridient")

if __name__ == '__main__':
    app.run(debug=True)


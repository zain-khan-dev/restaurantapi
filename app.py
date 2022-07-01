from flask import Flask
from flask_restful import Resource, Api

from resources.menu import Menu
from resources.menu import MenuList
from resources.order import Order
from resources.order import OrderList
from resources.inventory import Inventory
from resources.ingridients import Ingridient
from resources.ingridients import IngridientList
from resources.inventory import InventoryList

app = Flask(__name__)
api = Api(app)

api.add_resource(MenuList, "/menu")

api.add_resource(Menu, "/menu/<string:objectId>")

api.add_resource(OrderList, "/order")

api.add_resource(Order, "/order/<string:objectId>")

api.add_resource(InventoryList, "/inventory")

api.add_resource(Inventory, "/inventory/<string:objectId>")

api.add_resource(IngridientList, "/ingridient")

api.add_resource(Ingridient, "/ingridient/<string:objectId>")


if __name__ == '__main__':
    app.run(debug=True)


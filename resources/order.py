from flask import request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from config.dbconfig import db
from bson import json_util
from bson.objectid import ObjectId

import json
order_table = db["order"]
menu_table = db["menu"]


class Order(Resource):
    def get(self):
        items = order_table.find({})
        return json.loads(json_util.dumps(list(items)))

    def post(self):
        data = request.get_json()
        menu_items = [ObjectId(id) for id in data["menu_items"].split(",")]
        table_id = data["table_ids"]
        print(menu_items)
        print(list(menu_table.find({})))
        order_items = list(menu_table.find({"_id":{"$in":menu_items}}))
        print(order_items)
        order_id = order_table.insert_one({"menu_items":order_items,"table_id":table_id})
        return {'created order'}

    
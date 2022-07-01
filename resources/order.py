from flask import request, jsonify, Response
from flask_restful import reqparse, abort, Api, Resource
from config.dbconfig import db
from bson import json_util
from bson.objectid import ObjectId

import json
order_table = db["order"]
menu_table = db["menu"]


class OrderList(Resource):
    def get(self):
        items = order_table.find({})
        return json.loads(json_util.dumps(list(items)))

    def post(self):
        data = request.get_json()
        menu_items = [ObjectId(id) for id in data["menu_items"].split(",")]
        table_id = data["table_id"]
        order_items = list(menu_table.find({"_id":{"$in":menu_items}}))
        order_id = order_table.insert_one({"menu_items":order_items,"table_id":table_id})
        return {'created order'}


    

class Order(Resource):
    def delete(self, objectId):
        order_table.delete_one({"_id":ObjectId(objectId)})
        return Response({"deleted succsfully"}, status=200)

    def get(self,objectId):
        print(objectId)
        order = order_table.find_one({"_id":ObjectId(objectId)})
        return json.loads(json_util.dumps(order))

    def put(self, objectId):
        data = request.get_json()
        dict_to_update = {}
        if("table_id" in data.keys()):
            dict_to_update["table_id"] = data["table_id"]
        order_table.update_one({"_id":ObjectId(objectId)}, {"$set":dict_to_update})
        return Response({"Updated succesfully"}, status=204)  
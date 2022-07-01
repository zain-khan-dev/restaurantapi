from flask import request, jsonify, Response
from flask_restful import reqparse, abort, Api, Resource
from config.dbconfig import db
from bson import json_util
from bson.objectid import ObjectId
import json



inventory_table = db["inventory"]

ingridients_table = db["ingridients"]


class InventoryList(Resource):
       
    def get(self):
        items = inventory_table.find({})
        return json.loads(json_util.dumps(list(items)))

    def post(self):
        data = request.get_json()
        ingridientId = data["ingridient"]
        quantity = data["quantity"]
        ingridient = ingridients_table.find_one({"_id":ObjectId(ingridientId)})
        inventory = inventory_table.insert_one({"quantity":quantity,"ingridient":ingridient})
        return Response({"Added successfully"}, status=204)





class Inventory(Resource):
    def get(self, objectId):
        items = inventory_table.find_one({"_id":ObjectId(objectId)})
        return json.loads(json_util.dumps(order))

    def delete(self, objectId):
        inventory_table.delete_one({"_id":ObjectId(objectId)})
        return Response({"deleted succesfully"}, status=204)

    def put(self, objectId):
        data = request.get_json()
        dict_to_update = {}
        if("quantity" in data.keys()):
            dict_to_update["quantity"] = data["quantity"]
        inventory_table.update_one({"_id":ObjectId(objectId)}, {"$set":dict_to_update})
        return Response({"Updated succesfully"}, status=204)  
from flask import request, jsonify, Response
from flask_restful import reqparse, abort, Api, Resource
from config.dbconfig import db
from bson import json_util
from bson.objectid import ObjectId
import json



inventory_table = db["inventory"]

ingridients_table = db["ingridients"]


class Inventory(Resource):


    def get(self, id):
        items = inventory_table.find({"id_":ObjectId(id)})
        return json.loads(json_util.dumps(list(items)))        

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

    
    def delete(self):
        data = request.get_json()
        id = data["id"]
        inventory_table.delete_one({"_id":ObjectId(id)})
        return Response({"deleted succsfully"}, status=200)



    def put(self):
        data = request.get_json()
        id = data["id"]
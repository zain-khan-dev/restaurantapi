from flask import request, jsonify, Response
from flask_restful import reqparse, abort, Api, Resource
from config.dbconfig import db
from bson import json_util
from bson.objectid import ObjectId
import json


ingridients_table = db["ingridients"]


class IngridientList(Resource):
    def get(self):
        items = ingridients_table.find({})
        return json.loads(json_util.dumps(list(items)))

    def post(self):
        data = request.get_json()
        name = data["name"]
        description = data["description"]
        ingri = ingridients_table.insert_one({"name":name, "description":description})
        return Response({"Added successfully"}, status=204)


class Ingridient(Resource):
    def get(self, objectId):
        items = ingridients_table.find_one({"_id":ObjectId(objectId)})
        return json.loads(json_util.dumps(items))

    def delete(self, objectId):
        ingridients_table.delete_one({"_id":ObjectId(objectId)})
        return Response({"deleted succesfully"}, status=204)

    def put(self, objectId):
        data = request.get_json()
        dict_to_update = {}
        if("name" in data.keys()):
            dict_to_update["name"] = data["name"]
        if("description" in data.keys()):
            dict_to_update["description"] = data["description"]
        
        ingridients_table.update_one({"_id":ObjectId(objectId)}, {"$set":dict_to_update})
        return Response({"Updated succesfully"}, status=204)  




    
    # def delete(self):
    #     data = request.get_json()
    #     id = data["id"]
    #     menu_table.delete_one({"_id":ObjectId(id)})
    #     return Response({"deleted succsfully"}, status=200)

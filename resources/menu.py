from flask import request, jsonify, Response
from flask_restful import reqparse, abort, Api, Resource
from config.dbconfig import db
from bson import json_util
from bson.objectid import ObjectId
import json



menu_table = db["menu"]
ingridients_table = db["ingridients"]


class MenuList(Resource):
    def get(self):
        items = menu_table.find({})
        return json.loads(json_util.dumps(list(items)))

    def post(self):
        data = request.get_json()
        title = data["title"]
        description = data["description"]
        price = data["price"]
        ingridients = [ObjectId(id) for id in data["ingridients"].split(",")]
        ingridients_collection = list(ingridients_table.find({"_id":{"$in":ingridients}}))
        menu_id = menu_table.insert_one({"title":title,"description":description,"price":price, "ingridients":ingridients_collection})
        return jsonify({'data':data})

    

    def delete(self, objectId):
        data = request.get_json()
        id = data["id"]
        menu_table.delete_one({"_id":ObjectId(id)})



class Menu(Resource):


    def get(self, objectId):
        menu_item = menu_table.find_one({"_id":ObjectId(objectId)})
        return json.loads(json_util.dumps(menu_item))

    def delete(self, objectId):
        data = request.get_json()
        menu_table.delete_one({"_id":ObjectId(objectId)})
        return Response({"deleted succsfully"}, status=200)        


    def put(self, objectId):
        data = request.get_json()
        dict_to_update = {}
        if("title" in data.keys()):
            dict_to_update["title"] = data["title"]
        if("description" in data.keys()):
            dict_to_update["description"] = data["description"]
        if("price" in data.keys()):
            dict_to_update["price"] = data["price"]
        menu_table.update_one({"_id":ObjectId(objectId)}, {"$set":dict_to_update})
        return Response({"Updated succesfully"}, status=204)  




# 62bf1b4ff80006aaa0cf5512,62bf1b71511ede70bc876c81
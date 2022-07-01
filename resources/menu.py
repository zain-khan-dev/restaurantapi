from flask import request, jsonify, Response
from flask_restful import reqparse, abort, Api, Resource
from config.dbconfig import db
from bson import json_util
from bson.objectid import ObjectId
import json



menu_table = db["menu"]
ingridients_table = db["ingridients"]


class Menu(Resource):
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

    
    def delete(self):
        data = request.get_json()
        id = data["id"]
        menu_table.delete_one({"_id":ObjectId(id)})
        return Response({"deleted succsfully"}, status=200)

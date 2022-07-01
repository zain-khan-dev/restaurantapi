from flask import request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from config.dbconfig import db
from bson import json_util
import json
menu_table = db["menu"]

class Menu(Resource):
    def get(self):
        items = menu_table.find({})
        return json.loads(json_util.dumps(list(items)))

    def post(self):
        data = request.get_json()
        title = data["title"]
        description = data["description"]
        price = data["price"]
        menu_id = menu_table.insert_one({"title":title,"description":description,"price":price})
        return jsonify({'data':data})

    
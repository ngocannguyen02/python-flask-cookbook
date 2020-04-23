from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/recipes"
mongo = PyMongo(app)
collection = mongo.db.recipe

@app.route('/recipes')
def get_all_recipes():
    try:
        if collection.find().count() > 0:
            recipes_list = []
            for obj in collection.find():
                obj.pop('_id') # id object is not jsonify so we pop it out
                recipes_list.append(obj)
            return jsonify(recipes_list)
        else:
            return jsonify([])
    except:
        return "", 500

@app.route('/recipes', methods=['POST'])
def add_recipe():
    recipe = request.get_json()
    collection.insert(recipe)
    return {}, 200

@app.route('/recipes/<string:title>', methods=['PUT'])
def update_recipe(title):
    recipe = request.get_json()
    collection.save(recipe)
    return {}, 200

@app.route('/recipes/<string:title>', methods=['DELETE'])
def delete_recipe(title):
    collection.remove({"title": title})
    return 'None', 200

app.run()
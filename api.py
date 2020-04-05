from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO improve with a database integration

recipes = {
    "Steak and french fries" : 
    {
        "description": "The Shawshank Redemption",
        "ingredients": [ 
           {
               "name": "steak",
               "quantity": "1kg"
           },
           {
               "name": "french fries",
               "quantity": "150g"
           }
       ]
    },
    "Pizza" : 
    {
       "description": "The Godfather ",
       "ingredients": [ 
           {
               "name": "cheese",
               "quantity": "150g"
           },
           {
               "name": "tomato",
               "quantity": "150g"
           }
       ]
    }
}

@app.route('/recipes')
def get_all_recipes():
    return jsonify(recipes)

@app.route('/recipes', methods=['POST'])
def add_recipe():
    recipe = request.get_json()
    recipes[recipe["key"]["title"]] = recipe["recipe"]
    return {'id': len(recipes)}, 200

@app.route('/recipes/<string:title>', methods=['PUT'])
def update_recipe(title):
    recipe = request.get_json()
    recipes[title] = recipe
    return jsonify(recipes[title]), 200

@app.route('/recipes/<string:title>', methods=['DELETE'])
def delete_recipe(title):
    recipes.pop(title)
    return 'None', 200

app.run()
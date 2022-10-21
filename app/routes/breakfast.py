from flask import Blueprint, jsonify

class Breakfast():
    def __init__(self, id, name, rating, prep_time):
        self.id = id
        self.name = name
        self.rating = rating
        self.prep_time = prep_time

breakfast_item = [
    Breakfast(1, "omelette", 4, 10),
    Breakfast(2, "french toast", 3, 15),
    Breakfast(3, "cereal", 1, 1),
    Breakfast(4, "oatmeal", 3, 5)
]

breakfast_bp = Blueprint("breakfast", __name__, url_prefix="/breakfast")

@breakfast_bp.route('',methods=['GET'])
#breakfast_item is a global variable so we don't need to pass it in the function
def get_all_breakfasts():
    # return("hello world")
    #turning the list of breakfast_item and convert it to json
    #import jsonify 
    result = []
    for item in breakfast_item:
        item_dict = {"id" : item.id, "name": item.name, "rating": item. rating, "prep time": item.prep_time}
        result.append(item_dict)
        
    return jsonify(result), 200
    
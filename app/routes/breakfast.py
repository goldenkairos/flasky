from crypt import methods
from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.breakfast import Breakfast


'''
class Breakfast():
    def __init__(self, id, name, rating, prep_time):
        self.id = id
        self.name = name
        self.rating = rating
        self.prep_time = prep_time

breakfast_items = [
    Breakfast(1, "omelette", 4, 10),
    Breakfast(2, "french toast", 3, 15),
    Breakfast(3, "cereal", 1, 1),
    Breakfast(4, "oatmeal", 3, 5)
]
'''


breakfast_bp = Blueprint("breakfast", __name__, url_prefix="/breakfast")

@breakfast_bp.route('',methods=['GET'])
#breakfast_item is a global variable so we don't need to pass it in the function
def get_all_breakfasts():
    #turning the list of breakfast_item and convert it to json
    #import jsonify 
    result = []
    all_breakfasts = Breakfast.query.all()
    for item in all_breakfasts:
        # item_dict = {"id" : item.id, "name": item.name, "rating": item. rating, "prep time": item.prep_time}
        result.append(item.to_dict())
        
    return jsonify(result), 200


##We will work on this later
@breakfast_bp.route('/<breakfast_id>',methods=['GET']) #this is called decorator
#breakfast_item is a global variable so we don't need to pass it in the function
def get_one_breakfasts(breakfast_id): #pass the parameter for whatever we called in the ' ' in the decorator
    # try:
    #     breakfast_id = int(breakfast_id)
    # except ValueError: #ValueError (where we receive a string instead of an int)
    #     return jsonify({"message":f"in valid data type {breakfast_id} invalid"}), 400        
    
    # chosen_breakfast = Breakfast.query.get(breakfast_id)
    chosen_breakfast = get_breakfast_from_id(breakfast_id)

    # if chosen_breakfast is None:
    #     return jsonify({"message":f"Could not find breakfast item with id: {breakfast_id}"}), 404
        
    return jsonify(chosen_breakfast.to_dict()),200


@breakfast_bp.route('', methods=['POST'])
def create_one_breakfast():
    request_body = request.get_json()
    
    new_breakfast = Breakfast(name=request_body['name'],
                              rating=request_body['rating'],
                              prep_time=request_body['prep_time'])
    
    #adding this new record to the database
    db.session.add(new_breakfast)
    
    #tell databse to commit everything
    db.session.commit()
    
    return jsonify({'message': f"Successfully created Breakfast with id={new_breakfast.id}"}),201

@breakfast_bp.route('/<breakfast_id>', methods=['PUT'])
def update_breakfast(breakfast_id):
    update_breakfast = get_breakfast_from_id(breakfast_id)
    
    request_body = request.get_json()
    
    try:
        update_breakfast.name = request_body["name"]
        update_breakfast.rating = request_body["rating"]
        update_breakfast.prep_time = request_body["prep_time"]
    
    except KeyError: ##when the requesting body in "try" is missing one of the attributes
        return jsonify({"msg":"Missing needed data"}), 400 #we should think through of giving the user which attribute missing for meaningful feedback

    db.session.commit()
    
    return jsonify({"msg":f"Successfully updated breakfast with id {update_breakfast}"}), 200


@breakfast_bp.route('/<breakfast_id>', methods=['DELETE'])
def delete_one_breakfast(breakfast_id):
    breakfast_to_delete = get_breakfast_from_id(breakfast_id)

    db.session.delete(breakfast_to_delete)
    db.session.commit()
    
    return jsonify({"msg":f"Successfully delete breakfast with id {breakfast_to_delete.id} {breakfast_to_delete.name}"}, 200)
    
       
def get_breakfast_from_id(breakfast_id):
    try:
        breakfast_id = int(breakfast_id)
    except ValueError: #ValueError (where we receive a string instead of an int)
        return abort(make_response({"message":f"in valid data type {breakfast_id} invalid"}, 400)) 
    
    chosen_breakfast = Breakfast.query.get(breakfast_id)

    if chosen_breakfast is None:
        return abort(make_response({"message":f"Could not find breakfast item with id: {breakfast_id}"}, 404))
    
    return chosen_breakfast


from crypt import methods
from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.breakfast import Breakfast



breakfast_bp = Blueprint("breakfast", __name__, url_prefix="/breakfast")

@breakfast_bp.route('',methods=['GET'])
#breakfast_item is a global variable so we don't need to pass it in the function
def get_all_breakfasts():
    #turning the list of breakfast_item and convert it to json
    #import jsonify 
    
    rating_query_value = request.args.get("rating") #has to be a string to be passed in
    if rating_query_value is not None:
    
        breakfasts = Breakfast.query.filter_by(rating=rating_query_value)
    
    else:
        breakfasts = Breakfast.query.all()    
    
    result = []
    
    for item in breakfasts:
        # item_dict = {"id" : item.id, "name": item.name, "rating": item. rating, "prep time": item.prep_time}
        result.append(item.to_dict())
        
    return jsonify(result), 200


##We will work on this later
@breakfast_bp.route('/<breakfast_id>',methods=['GET']) #this is called decorator
#breakfast_item is a global variable so we don't need to pass it in the function
def get_one_breakfasts(breakfast_id): #pass the parameter for whatever we called in the ' ' in the decorator
    chosen_breakfast = get_model_from_id(Breakfast,breakfast_id)

    # if chosen_breakfast is None:
    #     return jsonify({"message":f"Could not find breakfast item with id: {breakfast_id}"}), 404
        
    return jsonify(chosen_breakfast.to_dict()),200


@breakfast_bp.route('', methods=['POST'])
def create_one_breakfast():
    #we will take the json format request and turn it into python dictionary
    request_body = request.get_json()
    
    #from the python dictionary, we turn this into a new Breakfast instance by using the request key to apply to the attribute of our Breakfast instance)
    # new_breakfast = Breakfast(name=request_body['name'],
    #                           rating=request_body['rating'],
    #                           prep_time=request_body['prep_time'])
    
    new_breakfast = Breakfast.from_dict(request_body) 
    
    #adding this new record to the database
    db.session.add(new_breakfast)
    
    #tell databse to commit everything
    db.session.commit()
    
    return jsonify({'message': f"Successfully created Breakfast with id = {new_breakfast.id}"}),201

@breakfast_bp.route('/<breakfast_id>', methods=['PUT'])
def update_breakfast(breakfast_id):
    update_breakfast = get_model_from_id(Breakfast,breakfast_id)
    
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
    breakfast_to_delete = get_model_from_id(Breakfast,breakfast_id)

    db.session.delete(breakfast_to_delete)
    db.session.commit()
    
    return jsonify({"msg":f"Successfully delete breakfast with id {breakfast_to_delete.id} {breakfast_to_delete.name}"}), 200
    
       
def get_model_from_id(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError: #ValueError (where we receive a string instead of an int)
        return abort(make_response({"message":f"invalid id for model of type {cls.__name__} {model_id} invalid"}, 400)) 
    
    chosen_object = cls.query.get(model_id)

    if chosen_object is None:
        return abort(make_response({"message":f"Could not find {cls.__name__} with id: {model_id}"}, 404))
    
    return chosen_object


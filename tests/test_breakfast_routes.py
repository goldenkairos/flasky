def test_get_all_breakfast_with_empty_db_return_empty_ist(client): #this is where we call client app from conftest.py
    response = client.get("/breakfast") #this mimic the GET endpoint to get all breakfast. Here we will have an empty database
    response_body = response.get_json() #make sure we have jsonify response
    
    assert response_body == []
    assert response.status_code == 200

def test_get_one_breakfast_with_empty_db_returns_404(client):
    response = client.get("/breakfast/1")
    response_body = response.get_json()
    
    assert response.status_code == 404
    assert "message" in response_body
    
def test_get_one_breakfast_with_populated_db_returns_breakfast_json(client,two_breakfasts): #passing in the fixture in conftest that we created for the db
    response = client.get("/breakfast/1")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name":"Water",
        "rating":2,
        "prep_time":1            
    }

def test_post_one_breakfast_creates_breakfast_in_db(client, two_breakfasts):
    response = client.post("/breakfast",json={
        "name":"Egg Casserole",
        "rating":5,
        "prep_time":90          
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert "message" in response_body
    assert response_body["message"] == "Successfully created Breakfast with id = 3"
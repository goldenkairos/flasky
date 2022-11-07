from app import db 

#breakfast is Many and Menu is one
class Breakfast(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    rating = db.Column(db.Float)
    prep_time = db.Column(db.Integer)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id')) #id should match whatever id name we have in Menu model
    menu = db.relationship('Menu', back_populates='breakfast_items')

    def to_dict(self):
    #this module is under Breakfast class. we can have different breakfast instances
    #this is an instance method
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "prep_time": self.prep_time
        }

#we want to create a method that turn a dictionary into a new instance. The to_dict() above is only from instance to dictionary.
#Let's create a CLASS METHOD
    @classmethod #classmethod decorator. When we call this function, we will populate an actual class itself.
    def from_dict(cls, breakfast_dict):  
        return cls(
            name=breakfast_dict["name"],
            rating=breakfast_dict["rating"],
            prep_time=breakfast_dict["prep_time"]        
        )
    
     #we can use below with the same resul. However, using cls() is better when we create a child class with more flexibility 
    # Breakfast(
        # name=breakfast_dict["name"],
        # rating=breakfast_dict["rating"],
        # prep_time=breakfast_dict["prep_time"])
        
        
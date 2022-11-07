from app import db

#breakfast is Many and Menu is one
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_name = db.Column(db.String)
    meal = db.Column(db.String)
    breakfast_item = db.relationship('Breakfast', back_populates=('menu'))
    
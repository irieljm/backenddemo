from project import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    #cannot be duplicated, is unique
    name = db.Column(db.String(50),unique=True) 
    #set limit so memory isn't oveloaded
    pin = db.Column(db.Integer, nullable=False) 
    #not nullable means neccessary
    balance = db.Column(db.Integer, default=0)
 
    def __repr__(self):
        return f"User(id='{self.id}', name='{self.name}', pin='{self.pin}', balance='{self.balance}')"
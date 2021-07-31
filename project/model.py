from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)   
    password = db.Column(db.String(100))
    username = db.Column(db.String(100))
    def __repr__(self):
        return "<User %r>" % self.email
        
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    is_comsumable = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(200))
    # label = db.Column(String(200))
    
class Item_register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    is_archive = db.Column(db.Boolean, nullable=False)
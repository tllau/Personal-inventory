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
    name = db.Column(db.String(100))
    is_comsumable = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_archive = db.Column(db.Boolean, nullable=False)
    # label = db.Column(String(200))
    def __repr__(self):
        return "<Item %r>" % self.name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Configure application
def create_app():
    app = Flask(__name__)
    app.secret_key = "b'\x0cZf\xcdg\xae\x884\xe5F\x08\xb62\x8b\n\xf4'"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) 
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
    
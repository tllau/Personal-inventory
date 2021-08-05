from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

# Configure application
def create_app():
    app = Flask(__name__)
    app.secret_key = "b'\x0cZf\xcdg\xae\x884\xe5F\x08\xb62\x8b\n\xf4'"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) 
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .model import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
    
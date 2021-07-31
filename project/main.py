from flask import Flask, flash, redirect, render_template, request, session, url_for, flash, Blueprint
from flask_login import login_required, login_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import timedelta
        
main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('index.html', name=current_user.username)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)
    
    
    


# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

# # User database
# class Users(UserMixin, db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(100), unique=True)       
    # def __repr__(self):
        # return "<User %r>" % self.email
        
# @login_manager.user_loader
# def load_user(user_id):
    # return Users.query.get(int(user_id))
    
    

# # Ensure responses aren't cached
# @app.after_request
# def after_request(response):
    # response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    # response.headers["Expires"] = 0
    # response.headers["Pragma"] = "no-cache"
    # return response
       
# @app.route("/")
# def index():
    # return render_template("index.html")

# @app.route("/admin")
# def admin():
    # return render_template("admin.html", users=Users.query.all())
    
# @app.route("/profile") 
# @login_required
# def profile():
    # if "email" in session:
        # return render_template("profile.html", email=session["email"])
    # else:
        # return redirect(url_for("login"))
  
# @app.route("/register", methods=['GET', 'POST'])
# def register():
    # if request.method == "POST": 
        # email = request.form["email"]
        # # check if email already registered
        # found_email = Users.query.filter_by(email=email).first()
        # if found_email:
            # flash("Email has already been used")
            # return redirect(url_for("register"))
        # else:        
            # usr = Users(email=email)
            # db.session.add(usr)
            # db.session.commit()
            # flash("Register sucessfully")
            # return redirect("/")
    # else:
        # return render_template("register.html")   
        
# @app.route("/login", methods=['GET', 'POST'])
# def login():
    # if request.method == "POST":
        # email = request.form["email"]
        # if Users.query.filter_by(email=email).first():
            # user = LoginManager.user_loader(email)
            # login_user(user)
            # flash("Login successfully")
            # return redirect("/")
        # else:
            # return redirect(url_for("login"))
    # else:
        # # if login in already
        # if "email" in session:
            # return redirect(url_for("index"))
        # else:
            # return render_template("login.html")
        
# @app.route("/logout")
# @login_required 
# def logout():
    # session.pop("email", None) 
    # flash("You have been logout.")    
    # return redirect(url_for("login"))
        
    
# if __name__ == "__main__":
    # db.create_all()
    # app.run(debug=True)
  


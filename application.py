from flask import Flask, flash, redirect, render_template, request, session, url_for, flash
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import timedelta
        
# Configure application
app = Flask(__name__)
app.secret_key = "b'\x0cZf\xcdg\xae\x884\xe5F\x08\xb62\x8b\n\xf4'"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.permanent_session_lifetime = timedelta(minutes=5)
db = SQLAlchemy(app)

# User database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
        
    def __repr__(self):
        return "<User %r>" % self.email
        
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader

def load_user(user_id):
    return User.get(user_id)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
       
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html", users=Users.query.all())
@app.route("/profile")  
def profile():
    if "email" in session:
        return render_template("profile.html", email=session["email"])
    else:
        return redirect(url_for("login"))
  
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST": 
        email = request.form["email"]
        # check if email already registered
        found_email = Users.query.filter_by(email=email).first()
        if found_email:
            flash("Email has already been used")
            return redirect(url_for("register"))
        else:        
            usr = Users(email=email)
            db.session.add(usr)
            db.session.commit()
            flash("Register sucessfully")
            return redirect("/")
    else:
        return render_template("register.html")       
@app.route("/login", methods=['GET', 'POST'])

def login():
    if request.method == "POST":
        email = request.form["email"]
        if Users.query.filter_by(email=email).first():
            session["email"] = email
            session.permanent = True
            flash("Login successfully")
            return redirect("/")
        else:
            return redirect(url_for("login"))
    else:
        # if login in already
        if "email" in session:
            return redirect(url_for("index"))
        else:
            return render_template("login.html")
        
@app.route("/logout") 
def logout():
    if "email" in session:
        session.pop("email", None) 
        flash("You have been logout.")    
    return redirect(url_for("login"))
        
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
  


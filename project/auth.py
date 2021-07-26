from flask import Blueprint, render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .model import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["inputPassword"] 
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already been used")
            return redirect(url_for("auth.register"))
        if not email or not username or not password:
            flash("Please fill in all mandatory field")
            return redirect(url_for("auth.register"))
        new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash("Register successfully")
        return redirect(url_for('auth.login'))
    else:
        return render_template('register.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')
from sqlite3 import IntegrityError

import flask_login
from blogapp import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from blogapp.forms import RegistrationForm, LoginForm
from blogapp.models import User, Post
from flask_login import login_required, login_user, current_user


@app.route("/test")
def test():
    return "<h1>Welcome, your flask app is working</h1>"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    else:
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
                "utf-8"
            )
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=hashed_password,
            )
            try:
                db.session.add(user)
                db.session.commit()
                flash("Registration successful!", "success")
                return redirect(url_for("login"))
            except IntegrityError:
                db.session.rollback()
                flash("Username or Email already exists.", "danger")

            flash(f"Account successfully created for {form.username.data}!", "success")
            return redirect(url_for("login"))
        # else:

        return render_template("accounts/register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    next_page = request.args.get("next")
                    return (
                        redirect(next_page) if next_page else redirect(url_for("home"))
                    )
                else:
                    flash("Login failed! Incorrect password.", "danger")
            else:
                flash("Login failed! Email not found.", "danger")
        return render_template("accounts/login.html", form=form)


@app.route("/logout")
def logout():
    flask_login.logout_user()
    flash("User logged out", "danger")
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    return "You are logged in"

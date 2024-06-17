from blogapp import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from blogapp.forms import RegistrationForm, LoginForm
from blogapp.models import User, Post


@app.route("/test")
def test():
    return "<h1>Welcome, your flask app is working</h1>"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        db.session.close()
        flash(f"Account successfully created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    # else:

    return render_template("accounts/register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Logged in successfully as {form.username.data}!", "success")
        return redirect(url_for("home"))
    else:
        flash("Login failed!", "danger")
    return render_template("accounts/login.html", form=form)


# @app.route("/logout")
# def logout():
#     flask_login.logout_user()
#     return "Logged out"

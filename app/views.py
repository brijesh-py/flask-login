from flask import redirect, render_template, request, url_for
from app import login_required, db, login_user, logout_user, current_user
from .models import Users
from datetime import datetime


def get_time():
    return datetime.now().strftime("%d-%b-%Y %H:%M")


@login_required
def home_view():
    return render_template("index.html")


def login_view():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")
        check_username = Users.query.filter_by(username=user).first()
        check_email = Users.query.filter_by(email=user).first()
        if check_username and check_username.check_password(password):
            login_user(check_username)
            return redirect("/")
        elif check_email and check_email.check_password(password):
            login_user(check_email)
            return redirect("/")
        else:
            return redirect(url_for("login", error="Invalid Username or Password?"))
    return render_template("login.html")


def join_view():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        check_username = Users.query.filter_by(username=username).first()
        check_email = Users.query.filter_by(email=email).first()
        if check_username or check_email:
            return redirect(url_for("join", error="Try anathor Username or Email?"))
        else:
            add_user = Users(
                username=username, email=email, password=password, created_at=get_time()
            )
            db.session.add(add_user)
            db.session.commit()
            return redirect(url_for("join", success="Successfuly Account created!"))
    return render_template("join.html")


@login_required
def logout_view():
    logout_user()
    return redirect("/login/")

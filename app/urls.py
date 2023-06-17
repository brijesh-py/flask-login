from app import app, login_manager, current_user
from .views import join_view, login_view, home_view, redirect, logout_view
from .models import Users


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


def check_user_exist(func):
    def wrapper(*args, **kwags):
        if current_user.is_active:
            return redirect("/")
        return func(*args, **kwags)

    return wrapper


@app.route("/")
def home():
    return home_view()


@app.route("/login/", methods=["GET", "POST"])
@check_user_exist
def login():
    return login_view()


@check_user_exist
@app.route("/join/", methods=["GET", "POST"])
def join():
    return join_view()



@app.route("/logout/")
def logout():
    return logout_view()
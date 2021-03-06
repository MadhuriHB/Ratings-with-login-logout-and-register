"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db

from flask import (Flask, render_template, redirect, request, flash,
                   session)

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/users")
def user_list():
    """ Show list of users """
    """ Grabs all the users from the db """
    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/register_form", methods=["GET"])
def register_form():

    return render_template("register_form.html")

@app.route("/register", methods=["POST"])
def register_process():
    username = request.form.get("user_name")
    password = request.form.get("password")
    users = User.query.filter_by(password=password).all()
    





    return redirect("/")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()

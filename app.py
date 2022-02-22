# ----- Libary Imports -----

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# ----- Flask App Configuration -----

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ----- Get tasks -----

@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find()
    return render_template("tasks/tasks.html", tasks=tasks)


# ----- Search function -----

@app.route("/search", methods=["GET", "POST"])
def search():
    """ Search tasks """
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("tasks/tasks.html", tasks=tasks)


# ----- Sign Up Page -----

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    Allows user to sign up for an account,
    rendering sign_up.html.
    Prevention of username duplicates included.
    """
    if "user" not in session:
        if request.method == "POST":
            # Check if username already exists
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get(
                    "username").lower()})

            # Prevents duplicates
            if existing_user:
                flash("Username already exists")
                return redirect(url_for("sign_up"))

            # Send collected data to user collection
            sign_up = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(sign_up)

            # Welcome user
            session["user"] = request.form.get("username").lower()
            flash("Welcome Onboard!")
            return redirect(url_for("profile",
                                    username=session["user"]))

        return render_template("users/sign_up.html")

    else:
        # If user logged in
        flash("You already have an account")
        return redirect(url_for("profile",
                                username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

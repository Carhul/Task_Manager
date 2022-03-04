"""
    A lot of the code is adapted and adjusted
    from the Code Institute learning material,
    especially the Task Manager Flask App mini Project
"""
import os
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

DEBUG_MODE = "DEBUG" in os.environ

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def login_required(f):
    """
    User login_required decorater adapted from:
    https://flask.palletsprojects.com/en/2.0.x/patterns/
    viewdecorators/#login-required-decorator

    Credit: sandeep_mentor
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("You need to Sign In to see this page!")
            return redirect(url_for("sign_in"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    """Get tasks from taskmanager_database."""
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks/tasks.html", tasks=tasks)


@app.route("/search", methods=["GET"])
def search():
    """Search tasks"""
    query = request.args.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("tasks/tasks.html", tasks=tasks)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    Credit:https://github.com/rebeccatraceyt/
    bake-it-til-you-make-it/blob/master/app.py

    Allows user to sign up for an account,
    rendering sign_up.html.
    Prevention of username duplicates included.
    """
    if "user" not in session:
        if request.method == "POST":
            # Check if username already exists
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()}
            )

            # Prevents duplicates
            if existing_user:
                flash("Username already exists")
                return redirect(url_for("sign_up"))

            # Send collected data to user collection
            new_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
            }
            mongo.db.users.insert_one(new_user)

            # Welcome user
            session["user"] = request.form.get("username").lower()
            flash("Welcome Onboard!")
            return redirect(url_for("profile", username=session["user"]))

        return render_template("users/sign_up.html")

    else:
        # If user logged in
        flash("You already have an account")
        return redirect(url_for("profile", username=session["user"]))


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    """Sign-In Page"""
    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        # Ensure hashed password matches user input
        if existing_user and check_password_hash(
            existing_user["password"], request.form.get("password")
        ):
            session["user"] = request.form.get("username").lower()
            flash(
                f"Hello, {request.form.get('username')}! "
                f"Have a good day at the office!"
            )
            return redirect(url_for("get_tasks", username=session["user"]))

        # Username doesn't exist
        flash("Incorrect Username and/or Password")
        return redirect(url_for("sign_in"))

    return render_template("users/sign_in.html")


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    """Profile Page"""
    if session["user"]:
        # Grab the session user's username from db
        username = mongo.db.users.find_one({"username": session["user"]})["username"]
        # Get the tasks for the user
        user_tasks = list(mongo.db.tasks.find({"created_by": session["user"]}))

        return render_template(
            "users/profile.html", username=username, user_tasks=user_tasks
        )


@app.route("/logout")
def logout():
    """Remove user from session cookie"""
    flash("You are now logged out! Have a nice day!")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/create_task", methods=["GET", "POST"])
@login_required
def create_task():
    """Create task"""
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "department_name": request.form.get("department_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Created")
        return redirect(url_for("get_tasks"))

    departments = mongo.db.departments.find().sort("department_name", 1)
    return render_template("tasks/create_task.html", departments=departments)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    """Edit task"""
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if request.method == "POST":
        if task["created_by"] == session["user"]:
            is_urgent = "on" if request.form.get("is_urgent") else "off"
            submit = {
                "department_name": request.form.get("department_name"),
                "task_name": request.form.get("task_name"),
                "task_description": request.form.get("task_description"),
                "is_urgent": is_urgent,
                "due_date": request.form.get("due_date"),
                "created_by": session["user"],
            }
            mongo.db.tasks.replace_one({"_id": ObjectId(task_id)}, submit)
            flash("Task Successfully Updated")
        else:
            return redirect(url_for("get_tasks"))

    departments = mongo.db.departments.find().sort("department_name", 1)
    return render_template("tasks/edit_task.html", task=task, departments=departments)


@app.route("/delete_task/<task_id>")
@login_required
def delete_task(task_id):
    """Delete task"""
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


@app.route("/get_departments")
def get_departments():
    """Get department"""
    departments = list(mongo.db.departments.find().sort("department_name", 1))
    return render_template(
        "departments/departments.html", departments=departments
    )


@app.route("/add_department", methods=["GET", "POST"])
@login_required
def add_department():
    """Add department"""
    if request.method == "POST":
        department = {"department_name": request.form.get("department_name")}
        mongo.db.departments.insert_one(department)
        flash("New Department Added")
        return redirect(url_for("get_departments"))

    return render_template("departments/add_department.html")


@app.route("/edit_department/<department_id>", methods=["GET", "POST"])
@login_required
def edit_department(department_id):
    """Edit department"""
    if request.method == "POST":
        submit = {"department_name": request.form.get("department_name")}
        mongo.db.departments.replace_one({"_id": ObjectId(department_id)}, submit)
        flash("Department Successfully Updated")
        return redirect(url_for("get_departments"))

    department = mongo.db.departments.find_one({"_id": ObjectId(department_id)})
    return render_template("departments/edit_department.html", department=department)


@app.route("/delete_department/<department_id>")
@login_required
def delete_department(department_id):
    """Delete category"""
    mongo.db.departments.delete_one({"_id": ObjectId(department_id)})
    flash("Department Successfully Deleted")
    return redirect(url_for("get_departments"))


@app.errorhandler(404)
def page_not_found(e):
    """
    404 error handler

    Credit:https://github.com/rebeccatraceyt/
    bake-it-til-you-make-it/blob/master/app.py
    """
    return render_template("error_handlers/404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    500 error handler

    Credit:https://github.com/rebeccatraceyt/
    bake-it-til-you-make-it/blob/master/app.py
    """
    return render_template("error_handlers//500.html"), 500


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=DEBUG_MODE
    )

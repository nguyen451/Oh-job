import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Custom filter: no need for usd filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mbti.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/mbti")
@login_required
def mbti():
    return apology("Todo", 404)


@app.route("/major")
@login_required
def major():
    return apology("Todo", 404)


@app.route("/login", methods = ["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # POST
    if request.method == "POST":

        # Exist user name and pw
        if not request.form.get("username") or not request.form.get("password"):
            return apology("Must provide username and password", 400)
        
        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure usename exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)
        
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Logout
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods = ["GET", "POST"])
def register():
    """Register user"""

    # Forget session
    session.clear()

    # User reached route post (by submitting information)
    if request.method == "POST":
        # Ensure username and password was provided
        if not request.form.get("username") or not request.form.get("password"):
            return apology("Must provide username and password", 400)
        
        # Ensure user true rewrite password
        elif not request.form.get("confirmation"):
            return apology("Must rewrite password", 400)
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("Password rewrite not true", 400)
        
        # Check if usename exists
        username = request.form.get("username")
        checkname = db.execute("SELECT username FROM users WHERE username = ?", username)
        if len(checkname) != 0:
            return apology("Username existed", 400)
        
        # Hash password
        hash = generate_password_hash(request.form.get("password"))

        # Save username and hash
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

        # redirect user to index
        return redirect("/")
    else:
        return render_template("register.html")

        

    

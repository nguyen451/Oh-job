import os
import json

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

OPTIONS = ["0", "1", "2", "3", "4", "5"]
QUESTIONS = ["Make decisions after considering other people's thoughts",
            "Be perceived as imaginative and creative",
            "Make decisions that involve people based on data and customer analysis",
            "Only do work with others when they agree to accept the relevant commitments",
            "Be quiet, calm and think alone",
            "Use clearly known measures in theory to do the job",
            "Make decisions based on logical thinking and analysis, not influenced by emotions",
            "Do not want to commit to completing the assigned work",
            "Think carefully before speaking",
            "Consider the possibilities that can happen and solve the problem",
            "Everyone judges you as a technological, intellectual person",
            "Think for a long time before deciding to solve the problem",
            "Think internally and emotionally, do not let outsiders see your thoughts",
            "You clearly stabilize the definitions and concept",
            "You always help people explore and understand how they feel about things/events",
            "You tend to change and act while deciding on work",
            "You rarely speak out or can do very little thinking, planning",
            "You learn different perspectives on events, issues or problems",
            "Use your senses and personal experiences to decide",
            "Based on the long-term limits of data-based plans to do work",
            "You tend to seek new friends",
            "You are inclined to people with many ideas",
            "You have made decisions based on personal beliefs",
            "Use notebooks, dating, work",
            "Discuss new issues and spend a long time thinking with the whole group before deciding",
            "You think, plan principles with high specificity",
            "When considering work, you do not let the situation and relationship with the person involved be suggested",
            "You do well when you are interested",
            "You tend to be the center of attention in a group",
            "You tend to fantasize about what might happen",
            "You tend to pay attention to emotions when watching movies or having conversations",
            "You tend to start meetings at a predetermined time"]

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mbti")
def mbti():
    return render_template("mbti.html")

@app.route("/test", methods = ["GET", "POST"])
@login_required
# is login required here? 
def test():
    # If user post all answer
    # missing: check for completed test : maybe using try except
    if request.method == "POST":
        # caculate I:
        try:
            I = 5 - int(request.form.get("1")) + int(request.form.get("5")) + int(request.form.get("9")) + int(request.form.get("13")) + int(request.form.get("17")) + 5 - int(request.form.get("21")) + 5 - int(request.form.get("25")) + 5 - int(request.form.get("29"))
            E = int(request.form.get("1")) + 5 - int(request.form.get("5")) + 5 - int(request.form.get("9")) + 5 - int(request.form.get("13")) + 5 - int(request.form.get("17")) + int(request.form.get("21")) + int(request.form.get("25")) + int(request.form.get("29"))
        
            N = int(request.form.get("2")) + 5 - int(request.form.get("6")) + int(request.form.get("10")) + int(request.form.get("14")) + int(request.form.get("18")) + 5 - int(request.form.get("26")) + int(request.form.get("22")) + int(request.form.get("30"))
            S = 5 - int(request.form.get("2")) + int(request.form.get("6")) + 5 - int(request.form.get("10")) + 5 - int(request.form.get("14")) + 5 - int(request.form.get("18")) + 5 - int(request.form.get("22")) + int(request.form.get("26")) + 5 - int(request.form.get("30"))
        
            T = int(request.form.get("3")) + int(request.form.get("7")) + int(request.form.get("11")) + 5 - int(request.form.get("15")) + 5 - int(request.form.get("19")) + 5 - int(request.form.get("23")) + int(request.form.get("27")) + 5 - int(request.form.get("31"))
            F = 5 - int(request.form.get("3")) + 5 - int(request.form.get("7")) + 5 - int(request.form.get("11")) + int(request.form.get("15")) + int(request.form.get("19")) + int(request.form.get("23")) + 5 - int(request.form.get("27")) + int(request.form.get("31"))
        
            P = int(request.form.get("4")) + int(request.form.get("8")) + int(request.form.get("12")) + int(request.form.get("16")) + int(request.form.get("20")) + 5 - int(request.form.get("24")) + 5 - int(request.form.get("28")) + 5 - int(request.form.get("32"))
            J = int(request.form.get("1")) + 5 - int(request.form.get("5")) + 5 - int(request.form.get("9")) + 5 - int(request.form.get("13")) + 5 - int(request.form.get("20")) + int(request.form.get("24")) + int(request.form.get("28")) + int(request.form.get("32"))
        
            I = 5 - int(request.form.get("1")) + int(request.form.get("5")) + int(request.form.get("9")) + int(request.form.get("13")) + int(request.form.get("17")) + 5 - int(request.form.get("21")) + 5 - int(request.form.get("25")) + 5 - int(request.form.get("29"))
            E = int(request.form.get("1")) + 5 - int(request.form.get("5")) + 5 - int(request.form.get("9")) + 5 - int(request.form.get("13")) + 5 - int(request.form.get("17")) + int(request.form.get("21")) + int(request.form.get("25")) + int(request.form.get("29"))
        
            N = int(request.form.get("2")) + 5 - int(request.form.get("6")) + int(request.form.get("10")) + int(request.form.get("14")) + int(request.form.get("18")) + 5 - int(request.form.get("26")) + int(request.form.get("22")) + int(request.form.get("30"))
            S = 5 - int(request.form.get("2")) + int(request.form.get("6")) + 5 - int(request.form.get("10")) + 5 - int(request.form.get("14")) + 5 - int(request.form.get("18")) + 5 - int(request.form.get("22")) + int(request.form.get("26")) + 5 - int(request.form.get("30"))
        
            T = int(request.form.get("3")) + int(request.form.get("7")) + int(request.form.get("11")) + 5 - int(request.form.get("15")) + 5 - int(request.form.get("19")) + 5 - int(request.form.get("23")) + int(request.form.get("27")) + 5 - int(request.form.get("31"))
            F = 5 - int(request.form.get("3")) + 5 - int(request.form.get("7")) + 5 - int(request.form.get("11")) + int(request.form.get("15")) + int(request.form.get("19")) + int(request.form.get("23")) + 5 - int(request.form.get("27")) + int(request.form.get("31"))
        
            P = int(request.form.get("4")) + int(request.form.get("8")) + int(request.form.get("12")) + int(request.form.get("16")) + int(request.form.get("20")) + 5 - int(request.form.get("24")) + 5 - int(request.form.get("28")) + 5 - int(request.form.get("32"))
            J = int(request.form.get("1")) + 5 - int(request.form.get("5")) + 5 - int(request.form.get("9")) + 5 - int(request.form.get("13")) + 5 - int(request.form.get("20")) + int(request.form.get("24")) + int(request.form.get("28")) + int(request.form.get("32"))
        except TypeError:
            flash("Must answer all questions")
            return render_template("test.html", questions = QUESTIONS, options = OPTIONS)
        # decide what mbti:
        if I > E:
            mbti = "I"
        else: 
            mbti = "E"

        if N > S:
            mbti = mbti + "N"
        else: 
            mbti = mbti + "S"

        if T > F:
            mbti = mbti + "T"
        else: 
            mbti = mbti + "F"

        if P > J:
            mbti = mbti + "P"
        else: 
            mbti = mbti + "J"
        
        # save user's result
        db.execute("INSERT INTO history_results (mbti, introvert, extravert, sensor, intuitive, perciever, judger, feeler, thinker) VALUES (?,?,?,?,?,?,?,?,?)",mbti,I,E,S,N,P,J,F,T)
        # cux we've just create the test so it will have tha maximun value id in the table, the test_id is not depend on users'id
        test_id = db.execute("SELECT MAX(id) FROM history_results")
        db.execute("INSERT INTO history_test (user_id, test_id) VALUES(?,?)", session["user_id"], test_id[0]["MAX(id)"])
        # render results page:
        return redirect("/results")
    return render_template("test.html", questions = QUESTIONS, options = OPTIONS)


# ???? need????
@app.route("/results")
@login_required
def intp():
    # get the max id test cuz it is the current working test
    result = db.execute("SELECT * FROM history_results WHERE id = (SELECT MAX(id) FROM history_results)")
    return render_template("results.html", result=result)
    

@app.route("/login", methods = ["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # POST
    if request.method == "POST":
        # Exist user name and pw
        if not request.form.get("username") or not request.form.get("password"):
            flash("Missing username or password")
            return render_template("login.html")
        
        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure usename exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("Incorrect password")
            return render_template("login.html")
        
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
            flash("Missing username or password")
            return render_template("register.html")
        
        # Ensure user true rewrite password
        elif not request.form.get("confirmation"):
            flash("Must rewrite password")
            return render_template("register.html")
        elif request.form.get("confirmation") != request.form.get("password"):
            flash("Incorrect password")
            return render_template("register.html")
        
        # Check if usename exists
        username = request.form.get("username")
        checkname = db.execute("SELECT username FROM users WHERE username = ?", username)
        if len(checkname) != 0:
            flash("Username existed")
            return render_template("register.html")
        
        # Hash password
        hash = generate_password_hash(request.form.get("password"))

        # Save username and hash
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

        # redirect user to index
        return redirect("/")
    else:
        return render_template("register.html")

        
@app.route("/account")
@login_required
def account():
    username = db.execute("SELECT username FROM users WHERE id=?", session["user_id"])

    result = db.execute("SELECT * FROM history_results WHERE id IN (SELECT test_id FROM history_test WHERE user_id =?)", session["user_id"])
    time = db.execute("SELECT timestamp FROM history_test WHERE user_id=?", session["user_id"])
    count = len(result)
    return render_template("account.html",username=username[0]["username"], result=result, time=time, count=count)


@app.route("/changePW", methods=["GET", "POST"])
@login_required
def changePW():

    if request.method == "POST":
        if not request.form.get("current_password"):
            flash("Must provide current password")
            return render_template("changePW.html")
        if not request.form.get("new_password"):
            flash("Must provide new password")
            return render_template("changePW.html")
        hash = db.execute("SELECT hash FROM users WHERE id=?", session["user_id"])
        if not check_password_hash(hash[0]["hash"], request.form.get("current_password")):
            flash("Incorrect password")
            return render_template("changePW.html")
        
        new_password = request.form.get("new_password")
        new_hash = generate_password_hash(new_password)
        db.execute("UPDATE users SET hash =? WHERE id=?", new_hash, session["user_id"])
        return redirect("/")
    else:
        return render_template("changePW.html")


@app.route("/changeUN", methods=["GET", "POST"])
@login_required
def changeUN():
    if request.method == "POST":
        if not request.form.get("password"):
            flash("Must provide password")
            return render_template("changeUN.html")
        if not request.form.get("new_username"):
            flash("Must provide new username")
            return render_template("changeUN.html")
        hash = db.execute("SELECT hash FROM users WHERE id=?", session["user_id"])
        if not check_password_hash(hash[0]["hash"], request.form.get("password")):
            flash("Incorrect password")
            return render_template("changeUN.html")
        newName = request.form.get("new_username")
        db.execute("UPDATE users SET username =? WHERE id=?", newName, session["user_id"])
        return redirect("/")
    else:
        return render_template("changeUN.html")

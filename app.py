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

OPTIONS = ["0", "1", "2", "3", "4", "5"]
QUESTIONS = ["Ra quyết định sau khi cân nhắc suy nghĩ của mọi người",
            "Được mọi người cho là người có trí tưởng tượng và sáng tạo",
            "Ra quyết định liên quan tới con người dựa trên số liệu và phân tích khách quan", 
            "Chỉ thực hiện công việc với người khác khi họ đã đồng ý chấp nhận các cam kết có liên quan", 
            "Lặng lẽ, trầm tĩnh suy tính một mình",
            "Sử dụng các biện pháp đã biết rõ trong lý thuyết để thực hiện công việc",
            "Ra quyết định dựa trên các suy nghĩ, phân tích logic, không bị ảnh hưởng bởi cảm xúc",
            "Không muốn cam kết hạn chót hoàn thành công việc được giao",
            "Suy nghĩ kỹ trước khi nói",
            "Cân nhắc về các khả năng có thể xảy ra rồi mới giải quyết các vấn đề",
            "Mọi người đánh giá bạn là người công bằng, lý trí", 
            "Suy nghĩ một thời gian dài trước khi ra quyết định giải quyết vấn đề", 
            "Suy nghĩ nội tại và tình cảm, không để cho người ngoài nhìn thấy được suy nghĩ của mình",
            "Bạn ưa thích các định nghĩa và khái niệm không rõ ràng", 
            "Bạn luôn giúp mọi người khám phá và hiểu họ cảm thấy như thế nào về sự vật/ sự việc",
            "Bạn có xu hướng thay đổi và linh hoạt trong việc ra quyết định", 
            "Bạn ít khi nói ra bên ngoài hoặc thể hiện rất ít các suy nghĩ, dự tính của mình", 
            "Bạn tìm hiểu các cách nhìn khác nhau về sự kiện, vấn đề hay tình huống",
            "Sử dụng các giác quan và trải nghiệm cá nhân để ra quyết định", 
            "Lên kế hoạch dài hạn dựa trên các số liệu để thực hiện công việc", 
            "Bạn có xu hướng thích gặp bạn mới", 
            "Bạn thiên về người có nhiều ý tưởng",
            "Bạn ra quyết định dựa trên niềm tin cá nhân",
            "Sử dụng sổ tay ghi các ghi nhớ, cuộc hẹn, công việc",
            "Thảo luận về các vấn đề mới và dnahf thời gian dài suy nghĩ cùng cả nhóm trước khi ra quyết định",
            "Bạn suy nghĩ, hoạch định kế hoạch cẩn thận với sụ chính xác cao",
            "Khi cân nhắc công việc, bạn không để ý tới hoàn cảnh và mối quan hệ với người có liên quan",
            "Bạn sẽ làm tốt nếu như có hứng thú",
            "Bạn có thiên hướng trở thành trung tâm của nhóm",
            "Bạn có thiên hướng tưởng tượng về những gì có thể xảy ra",
            "Bạn thường chú trọng đến cảm xúc khi xem phim hay đối thoại",
            "Bạn thường bắt đầu buổi họp với thời gian định trước"]

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
def mbti():
    return render_template("mbti.html")

@app.route("/test", methods = ["GET", "POST"])
@login_required
# is login required here? 
def test():
    # If user post all answer
    if request.method == "POST":
        return apology("Todo", 404)
    return render_template("test.html", questions = QUESTIONS, options = OPTIONS)

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

        

    

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# =========================
# User Node
# =========================

class UserNode:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.next = None


# =========================
# User Linked List
# =========================

class UserList:

    def __init__(self):
        self.head = None

    def add_user(self, username, password):

        new_user = UserNode(username, password)

        if self.head is None:
            self.head = new_user
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_user

    def check_login(self, username, password):

        current = self.head

        while current is not None:

            if current.username == username and current.password == password:
                return True

            current = current.next

        return False

    def username_exists(self, username):

        current = self.head

        while current is not None:

            if current.username == username:
                return True

            current = current.next

        return False


# Create User List
users = UserList()


# =========================
# Event Registration Node
# =========================

class Node:

    def __init__(
        self,
        name,
        age,
        mobile,
        email,
        college,
        course,
        event
    ):

        self.name = name
        self.age = age
        self.mobile = mobile
        self.email = email
        self.college = college
        self.course = course
        self.event = event
        self.next = None


# =========================
# Event Registration List
# =========================

class EventRegistrationList:

    def __init__(self):
        self.head = None

    def add_registration(
        self,
        name,
        age,
        mobile,
        email,
        college,
        course,
        event
    ):

        new_node = Node(
            name,
            age,
            mobile,
            email,
            college,
            course,
            event
        )

        if self.head is None:

            self.head = new_node

        else:

            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def get_all_registrations(self):

        registrations = []

        current = self.head

        while current is not None:

            registrations.append({
                "name": current.name,
                "age": current.age,
                "mobile": current.mobile,
                "email": current.email,
                "college": current.college,
                "course": current.course,
                "event": current.event
            })

            current = current.next

        return registrations


registrations = EventRegistrationList()


# =========================
# Home Page
# =========================

@app.route("/")
def home():

    return render_template("index.html")


# =========================
# Sign Up
# =========================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if users.username_exists(username):

            return render_template(
                "signup.html",
                error="Username already exists!"
            )

        users.add_user(username, password)

        return redirect(url_for("home"))

    return render_template("signup.html")


# =========================
# Login
# =========================

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    if users.check_login(username, password):

        return redirect(url_for("register"))

    return render_template(
        "index.html",
        error="Invalid username or password!"
    )


# =========================
# Registration
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        age = request.form.get("age")
        mobile = request.form.get("mobile")
        email = request.form.get("email")
        college = request.form.get("college")
        course = request.form.get("course")
        event = request.form.get("event")

        registrations.add_registration(
            name,
            age,
            mobile,
            email,
            college,
            course,
            event
        )

        return redirect(url_for("registration_list"))

    return render_template("register.html")


# =========================
# Registration List
# =========================

@app.route("/list")
def registration_list():

    students = registrations.get_all_registrations()

    return render_template(
        "list.html",
        students=students
    )


# =========================
# Run
# =========================

if __name__ == "__main__":
    app.run(debug=True)
from functools import wraps

from flask import Flask, redirect, request, session, url_for

PASSWORD = "password"
PASSWORD_KEY = "passworkd_key"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

@app.route("/")
def index():
    return "Index"

@app.route("/login")
def login():
    session[PASSWORD_KEY] = PASSWORD
    if session.get(PASSWORD_KEY) == PASSWORD:
        return redirect(request.args["next"])
    return "Password incorrect"

@app.route("/private-page")
def private_page():
    if not session.get(PASSWORD_KEY) == PASSWORD:
        return redirect(url_for("login"))
    return "You need to log in to see this page"

if __name__ == "__main__":
    app.run()
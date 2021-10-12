from flask import Flask, redirect, url_for

app = Flask(__name__)
# app.config["SECRET_KEY"] = "secret"

@app.route("/")
def index():
    return "Index"

@app.route("/redirect")
def redirect_client():
    return redirect(url_for("endpoint"))

@app.route("/endpoint")
def endpoint():
    return "Endpoint"

if __name__ == "__main__":
    app.run()
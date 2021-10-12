import os
import subprocess

import flask
from flask import Flask, request, url_for

app = Flask(__name__)

def redirect(url):
    if url.startswith("/") and (gitpod_url:=os.environ.get("GITPOD_WORKSPACE_URL")):
        port = request.url_root.lstrip("http://localhost:")[:4]
        gitpod_url = subprocess.check_output(f"gp url {port}", shell=True).decode("utf-8")
        print(gitpod_url.strip() + url)
        return redirect(gitpod_url.strip() + url)

    return flask.redirect(url)

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
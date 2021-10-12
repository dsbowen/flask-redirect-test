import os
import subprocess

import flask
from flask import Flask, request, url_for

def redirect(url):
    if url.startswith("/") and "GITPOD_HOST" in os.environ:
        port = request.url_root.lstrip("http://localhost:")[:4]
        gp_url_port = subprocess.check_output(f"gp url {port}", shell=True)
        return flask.redirect(gp_url_port.decode("utf-8").strip() + url)

    return flask.redirect(url)

app = Flask(__name__)

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
# from asyncio.windows_events import NULL
import os
import datetime
# from shutil import unregister_unpack_format
# from socket import SCM_J1939_DEST_ADDR
from unicodedata import name

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///TODO")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")


@app.route("/location", methods=["GET", "POST"])
def location():
    return render_template("location.html")


@app.route("/rooms-cabins", methods=["GET", "POST"])
def rooms_cabins():
    return render_template("rooms-cabins.html")


@app.route("/our-story", methods=["GET", "POST"])
def our_story():
    return render_template("ourstory.html")


@app.route("/cabins", methods=["GET", "POST"])
def quote():
    return render_template("cabins.html")


@app.route("/rooms", methods=["GET", "POST"])
def register():
    return render_template("rooms.html")


@app.route("/oceanfront", methods=["GET", "POST"])
def sell():
    return render_template("oceanfront.html")


@app.route("/forest-view", methods=["GET", "POST"])
def change_password():
    return render_template("forest-view.html")

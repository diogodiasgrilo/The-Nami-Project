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
db = SQL("sqlite:///TODO")


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
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    if not db.execute(
            "SELECT * FROM users WHERE id = ?", user_id):
        return render_template("register.html")

    username = (db.execute(
        "SELECT username FROM users WHERE id = ?", user_id))[0]['username']

    if not db.execute("SELECT * FROM purchases WHERE username = ?", username):
        return render_template("buy.html")

    total = db.execute(
        "SELECT total FROM purchases WHERE username = ? GROUP BY total", username)

    total_len = len(total)

    total_added = 0

    # Figures out how much money the user has in stocks
    for i in range(total_len):
        j = total[i]
        j = j['total']
        total_added = total_added + j

    # Gathers a table with all the current stocks and amount of shares that the current logged in user has
    stocks = db.execute(
        "SELECT symbol, shares, name, price, total FROM purchases WHERE username = ? AND shares > 0", username)

    user_cash = (db.execute("SELECT cash FROM users WHERE id = ?", user_id))[
        0]['cash']

    total_added = total_added + user_cash

    return render_template("index.html", user_cash=usd(user_cash), stocks=stocks, total_added=usd(round(total_added, 2)))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # Does some checks to see if the input for the buy function was valid
        if not request.form.get("symbol"):
            return apology("please input a symbol")

        if not lookup(request.form.get("symbol")):
            return apology("stock symbol does not exist")

        if not request.form.get("shares"):
            return apology("please input a number of shares")

        if request.form.get("shares").isnumeric() == False:
            return apology("please input a valid numeric number for shares")

        shares = int(request.form.get("shares"))

        if shares <= 0:
            return apology("please input at least one share")

        # Starts gathering information on the desired stock to buy
        symbol = request.form.get("symbol")
        stock_info = lookup(symbol)
        name = stock_info['name']
        price = stock_info['price']

        user_id = session["user_id"]

        user_cash = (db.execute("SELECT cash FROM users WHERE id = ?", user_id))[
            0]['cash']

        username = (db.execute(
            "SELECT username FROM users WHERE id = ?", user_id))[0]['username']

        total_cost = shares * price

        amount_left = user_cash - total_cost

        if user_cash < total_cost:
            return apology("you don't have enough money to make this purchase")

        # Updates the current user's purchases table to reflect the bought stock's amount and shares
        count = 0

        if db.execute("SELECT * FROM purchases"):
            symbols = db.execute("SELECT symbol FROM purchases")
            for s in symbols:
                s = s['symbol']
                if symbol == s:
                    db.execute(
                        "UPDATE purchases SET shares = ROUND(shares + ?, 2) WHERE symbol = ?", shares, symbol)
                    db.execute(
                        "UPDATE purchases SET total = ROUND(total + ?, 2) WHERE symbol = ?", total_cost, symbol)
                    count += 1

        if count == 0:
            db.execute(
                "INSERT INTO purchases (username, symbol, name, shares, price, total) VALUES(?, ?, ?, ?, ?, ?)", username, symbol, name, shares, price, total_cost)

        # Updates the current logged in user's cash balance
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   amount_left, user_id)

        # Inputs a row of information into the history table to reflect this user's purchase
        date = ((datetime.datetime.now()).strftime("%d-%m-%Y "))

        hour = ((datetime.datetime.now()).strftime("%I:%M:%S"))

        db.execute(
            "INSERT INTO history (username, symbol, shares, price, transacted) VALUES(?, ?, ?, ?, ?)", username, symbol, shares, round(price, 2), (date + hour))

        return redirect("/")

    else:

        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    # Gathers a table of the history of buys and sells that the current logged in user has ever done on this website
    username = (db.execute(
        "SELECT username FROM users WHERE id = ?", user_id))[0]['username']

    history = db.execute("SELECT * FROM history WHERE username = ?", username)

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        # Does some checks to see if the symbol that the user input was valid
        if not request.form.get("symbol"):
            return apology("please input a symbol")

        if not lookup(request.form.get("symbol")):
            return apology("stock symbol does not exist")
        else:
            # Looks up the symbol that the user requested and its current price
            symbol = request.form.get("symbol")
            stock_info = lookup(symbol)
            price = stock_info['price']
            price = round(price, 2)

            return render_template("quoted.html", name=stock_info['name'], price=usd(price), symbol=stock_info['symbol'])
    else:

        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("please input a username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("please input a password")

        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        if len(rows) > 0:
            return apology("username already taken")

        # Access form data
        username = request.form.get("username")

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match", 400)

        password_hash = generate_password_hash(
            request.form.get("password"), method='pbkdf2:sha1', salt_length=8)

        db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)", username, password_hash)

        session["user_id"] = (db.execute(
            "SELECT * FROM users WHERE username = ?", username))[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        # Does some checks to see if the input for the buy function was valid
        if not request.form.get("symbol"):
            return apology("please choose a symbol")

        if not request.form.get("shares"):
            return apology("please input a number of shares")

        # Starts gathering information on the desired stock to buy
        shares = int(request.form.get("shares"))
        symbol = request.form.get("symbol")

        user_id = session["user_id"]
        username = (db.execute(
            "SELECT username FROM users WHERE id = ?", user_id))[0]['username']

        user_shares = (db.execute(
            "SELECT shares FROM purchases WHERE symbol = ? AND username = ?", symbol, username))[0]['shares']

        if shares < 1:
            return apology("please input at least one share")

        if shares > user_shares:
            return apology("you don't have that many shares")

        price = (lookup(symbol))['price']

        user_cash = (db.execute("SELECT cash FROM users WHERE id = ?", user_id))[
            0]['cash']

        total_sold = round((shares * price), 2)

        account_total = round((user_cash + total_sold), 2)

        # Updates the current user's purchases table to reflect this buy action
        count = 0

        symbols = db.execute(
            "SELECT symbol FROM purchases WHERE username = ?", username)
        for s in symbols:
            s = s['symbol']
            if symbol == s:
                db.execute(
                    "UPDATE purchases SET shares = ROUND(shares - ?, 2) WHERE symbol = ? AND username = ?", shares, symbol, username)
                db.execute(
                    "UPDATE purchases SET total = ROUND(total - ?, 2) WHERE symbol = ? AND username= ?", total_sold, symbol, username)
                count += 1

        share_check = (db.execute(
            "SELECT shares FROM purchases WHERE symbol = ? AND username = ?", symbol, username))[0]["shares"]

        if share_check <= 0:
            db.execute(
                "DELETE FROM purchases WHERE symbol = ? AND username = ?", symbol, username)

        # Updates the current logged in user's cash balance
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   account_total, user_id)

        # Inputs a row of information into the history table to reflect this user's purchase
        date = ((datetime.datetime.now()).strftime("%d-%m-%Y "))

        hour = ((datetime.datetime.now()).strftime("%I:%M:%S"))

        db.execute(
            "INSERT INTO history (username, symbol, shares, price, transacted) VALUES(?, ?, ?, ?, ?)",
            username, symbol, -abs(shares), round(price, 2), (date + hour))

        return redirect("/")

    else:

        username = (db.execute(
            "SELECT username FROM users WHERE id = ?", session["user_id"]))[0]['username']

        # Shows to the user only the stocks that the user still has more than 0 shares of
        symbols = db.execute(
            "SELECT symbol FROM purchases WHERE username = ? AND shares > 0", username)

        clean_symbols = []

        for i in symbols:
            clean_symbols.append(i['symbol'])

        return render_template("sell.html", symbols=clean_symbols)


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    """Allow the user to change their password"""
    if request.method == "POST":

        # Does some checks asking to see if the user still knows their old password in order to change it
        if request.form.get("new password") != request.form.get("confirm new password"):
            return apology("confirmation fields don't match")

        # Makes sure none of the fields are empty
        if not request.form.get("old password") or not request.form.get("new password") or not request.form.get("confirm new password"):
            return apology("one or more fields missing")

        username = (db.execute(
            "SELECT username FROM users WHERE id = ?", session["user_id"]))[0]['username']

        current_password = (db.execute(
            "SELECT hash FROM users WHERE username = ?", username))[0]['hash']

        # Compares the password that the user input as their old password with the current hash in the users table for this username to see if they match
        if check_password_hash(current_password, request.form.get("old password")) == False:
            return apology("current password doesn't match input")

        new_password_hash = generate_password_hash(
            request.form.get("new password"), method='pbkdf2:sha1', salt_length=8)

        # Updates the users table to now reflect the hash of the new password for the current username of the user that is logged in
        db.execute(
            "UPDATE users SET hash = ? WHERE username = ?", new_password_hash, username)

        return redirect("/")

    else:
        return render_template("change_password.html")

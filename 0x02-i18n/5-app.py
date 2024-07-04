#!/usr/bin/env python3
"""task 3: basic flask app"""
from flask import Flask, request, render_template, g
from flask_babel import Babel


class Config:
    """Babel configuration for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """sets default locale"""
    locale = request.args.get("locale", "")

    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def welcome():
    """prints 'Welcome to Holberton'"""
    return render_template("5-index.html")


def get_user():
    """get user"""
    user_id = request.args.get("login_as")
    if user_id:
        user = users[int(user_id)]
        return user
    return None


@app.before_request
def before_request():
    """gets the user and stores it globally"""
    user = get_user()
    if user:
        g.user = user


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

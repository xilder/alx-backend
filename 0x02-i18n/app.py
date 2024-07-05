#!/usr/bin/env python3
"""task 3: basic flask app"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, format_datetime
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError


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
    3: {"name": "Spock", "locale": "fr", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """sets default locale"""
    locale = request.args.get("locale", "")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]
    header_locale = request.headers.get("locale", None)
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])



@babel.timezoneselector
def get_timezone():
    """gets the timezone"""
    tz = request.args.get("timezone", None)
    if not tz and g.user["timezone"]:
        tz = g.user["timezone"]
    try:
        return timezone(tz).zone
    except UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/")
def welcome():
    """prints 'Welcome to Holberton'"""
    g.time = format_datetime()
    return render_template("index.html")
    # return g.user/


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

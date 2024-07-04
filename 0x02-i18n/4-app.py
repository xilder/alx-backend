#!/usr/bin/env python3
"""task 4: basic flask app"""
from flask import Flask, request, render_template, g
from flask_babel import Babel


class Config(object):
    """Babel configuration for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Gets the best matching locale for a web page"""
    locale = request.args.get("locale", "")

    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def welcome():
    """prints 'Welcome to Holberton'"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)

#!/usr/bin/env python3
from flask import Flask, request, render_template
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


@babel.localeselector
def get_locale():
    """sets default locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def welcome():
    """prints 'Welcome to Holberton"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()

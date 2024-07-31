#!/usr/bin/env python3
"""Babel Config Module"""
from flask_babel import Babel
from flask import Flask, render_template


class config():
    """Represents a Flask Babel configuration."""
    languages = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    
    
app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)


@app.route('/')
def home () -> str:
    """Home route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
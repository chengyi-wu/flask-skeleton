import os

from flask import Flask, render_template
from . import home

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(home.bp)

    return app
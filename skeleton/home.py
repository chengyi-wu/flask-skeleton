import functools

from flask import Flask, render_template, Blueprint

bp = Blueprint('home', __name__)

@bp.route('/')
@bp.route('/home')
@bp.route('/home/index')
def index():
    return render_template('home/index.html', msg="text area")
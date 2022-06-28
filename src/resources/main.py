from flask import render_template, make_response, redirect, url_for, flash, Blueprint, request
from flask_login import current_user


main = Blueprint('main', __name__)


@main.route('/', methods=["GET"])
def index():
    """
    Index Resource. Render the 'index.html' landing page.
    """

    return "Hello World", 200

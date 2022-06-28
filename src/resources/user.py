from flask import render_template, make_response, redirect, url_for, flash, Blueprint, request
from flask_login import login_user, logout_user, current_user
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                get_jwt,
                                set_refresh_cookies,
                                set_access_cookies,
                                jwt_required)


user = Blueprint('user', __name__)


@user.route('/register', methods=["GET", "POST"])
def register():
    """
    Register a new user.
    """

    return "/register", 200


@user.route('/login', methods=["GET", "POST"])
def login():
    """
    Login a new user.
    """

    return "/login", 200

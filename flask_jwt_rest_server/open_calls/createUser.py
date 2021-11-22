from flask import request, g
from flask.app import _Status
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.connect_db import createUser
from tools.token_tools import create_token

from tools.logging import logger
from db_con import get_db_instance, get_db

def handle_request():
    logger.debug("createUser Handle Request")

    password_from_user_form = request.form['password']
    uName = request.form['firstname']

    createUser(uname, password_from_user_form)
    return json_response(_Status = "Good", message = 'User Sucessfully Created')
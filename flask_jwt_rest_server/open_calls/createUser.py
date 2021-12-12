from flask import request, g
#from flask.app import _Status
from flask_json import FlaskJSON, JsonError, json_response, as_json
#from flask_jwt_rest_server.tools.connect_db import checkExist
from tools.connect_db import createUser, checkExist
from tools.token_tools import create_token

from tools.logging import logger
from db_con import get_db_instance, get_db

def handle_request():
    logger.debug("createUser Handle Request")

    password_from_user_form = request.form['password']
    uName = request.form['firstname']

    if checkExist(uName):
        return json_response(_status_ = "Error", message = 'User already exists.')

    createUser(uName, password_from_user_form)
    return json_response(_status_ = "Good", message = 'User Sucessfully Created')
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_jwt_rest_server.tools.connect_db import checkAuth
from tools.token_tools import create_token

from tools.logging import logger
from db_con import get_db_instance, get_db
from tools import connect_db

def handle_request():
    logger.debug("Login Handle Request")
    #use data here to auth the user

    password_from_user_form = request.form['password']
    uName = request.form['firstname']
    
    if checkAuth(uName, password_from_user_form):
        user = {
                "sub" : request.form['firstname'] #sub is used by pyJwt as the owner of the token
                }

    if not user:
        return json_response(status_=401, message = 'Invalid credentials', authenticated =  False )



    return json_response( token = create_token(user) , authenticated = True)


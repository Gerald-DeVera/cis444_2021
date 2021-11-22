from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
import datetime
from tools.connect_db import purchase

from tools.logging import logger

def handle_request():
    logger.debug("buy_book Handle Request")
    
    curUser = "test"
    #curUser = request.form['userName']
    bookName = request.form['book_id']
    time = datetime.datetime.now()

    purchase(curUser, bookName, time)

    return json_response(message = "Sucess")

    


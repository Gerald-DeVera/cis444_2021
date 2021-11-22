from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token

from tools.logging import logger
from db_con import get_db_instance, get_db

def checkAuth(user, passw):
    logger.debug("Checking to auth user")

    cur = global_db_con.cursor()
	dbEntry = "SELECT password FROM users WHERE username ='"
	dbEntry += request.form['uname']
	dbEntry += "';"
	cur.execute(dbEntry)
    r = cur.fetchone()
    upass = str(r[0])

    if bcrypt.checkpw(bytes(passw, 'utf-8'), upass.encode('utf-8')):
        return True
    return False

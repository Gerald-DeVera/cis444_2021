from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token

from tools.logging import logger
from db_con import get_db_instance, get_db

import jwt
import bcrypt


global_db_con = get_db()

def checkAuth(user, passw):
    logger.debug("Checking to auth user")

    cur = global_db_con.cursor()
    dbEntry = "SELECT password FROM users WHERE username ='"
    dbEntry += user
    dbEntry += "';"
    cur.execute(dbEntry)
    r = cur.fetchone()
    upass = str(r[0])

    if bcrypt.checkpw(bytes(passw, 'utf-8'), upass.encode('utf-8')):
        return True
    return False

def createUser(user, passw):
    logger.debug("Creating a new User")

    salted = bcrypt.hashpw(bytes(request.form['pass'], 'utf-8'), bcrypt.gensalt(10))

    cur = global_db_con.cursor()
    dbEntry = "INSERT INTO users(username, password) VALUES('"
    dbEntry += str(user)
    dbEntry += "','"
    dbEntry += str(salted.decode('utf-8'))
    dbEntry += "');"

    logger.debug(dbEntry)



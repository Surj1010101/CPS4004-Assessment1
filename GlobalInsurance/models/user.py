import sqlite3
from sqlite3 import Error
import bcrypt

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def add_user(conn, user):
    """
    Create a new user
    :param conn:
    :param user:
    :return:
    """
    sql = ''' INSERT INTO users(username, password, role)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    hashed_password = bcrypt.hashpw(user[1].encode('utf-8'), bcrypt.gensalt())
    cur.execute(sql, (user[0], hashed_password, user[2]))
    conn.commit()
    return cur.lastrowid

def authenticate_user(conn, username, password):
    """
    Authenticate a user
    :param conn:
    :param username:
    :param password:
    :return:
    """
    sql = ''' SELECT * FROM users WHERE username = ? '''
    cur = conn.cursor()
    cur.execute(sql, (username,))
    user = cur.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[2]):
        return user
    return None
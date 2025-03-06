import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def add_policy(conn, policy):
    """
    Create a new policy.
    :param conn: Database connection
    :param policy: Tuple containing policy details
    :return: Last row id of the inserted policy
    """
    sql = ''' INSERT INTO policies(policy_number, coverage_details, policy_limits)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, policy)
    conn.commit()
    return cur.lastrowid

def update_policy(conn, policy):
    """
    Update an existing policy.
    :param conn: Database connection
    :param policy: Tuple containing updated policy details
    """
    sql = ''' UPDATE policies
              SET policy_number = ?,
                  coverage_details = ?,
                  policy_limits = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, policy)
    conn.commit()
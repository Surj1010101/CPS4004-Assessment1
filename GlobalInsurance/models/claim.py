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

def add_claim(conn, claim):
    """
    Create a new claim.
    :param conn: Database connection
    :param claim: Tuple containing claim details
    :return: Last row id of the inserted claim
    """
    sql = ''' INSERT INTO claims(claim_number, 
                                date_of_claim, 
                                type_of_claim, 
                                description_of_accident, 
                                date_of_incident, location, 
                                incident_report, claim_amount, 
                                approved_amount, payment_details)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, claim)
    conn.commit()
    return cur.lastrowid

def update_claim(conn, claim):
    """
    Update an existing claim.
    :param conn: Database connection
    :param claim: Tuple containing updated claim details
    """
    sql = ''' UPDATE claims
              SET claim_number = ?,
                  date_of_claim = ?,
                  type_of_claim = ?,
                  description_of_accident = ?,
                  date_of_incident = ?,
                  location = ?,
                  incident_report = ?,
                  claim_amount = ?,
                  approved_amount = ?,
                  payment_details = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, claim)
    conn.commit()
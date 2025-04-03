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

def add_claim(conn, claim_data):
    """
    Create a new claim.
    :param conn: Database connection
    :param claim_data: Tuple with fields matching the columns in claims table
    :return: Last row id of the inserted claim
    """
    sql = """ INSERT INTO claims(
        claim_number, date_of_claim, type_of_claim, description_of_accident,
        date_of_incident, location, incident_report, claim_amount,
        approved_amount, payment_details, claim_status, resolution_notes, settlement_date
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, claim_data)
    conn.commit()
    return cur.lastrowid

def update_claim(conn, updated_data):
    """
    Update an existing claim.
    :param conn: Database connection
    :param updated_data: Tuple containing new claim fields + the claim ID
    """
    sql = """ UPDATE claims
              SET claim_number=?,
                  date_of_claim=?,
                  type_of_claim=?,
                  description_of_accident=?,
                  date_of_incident=?,
                  location=?,
                  incident_report=?,
                  claim_amount=?,
                  approved_amount=?,
                  payment_details=?,
                  claim_status=?,
                  resolution_notes=?,
                  settlement_date=?
              WHERE id=? """
    cur = conn.cursor()
    cur.execute(sql, updated_data)
    conn.commit()

def get_claim(conn, claim_id):
    """
    Retrieve a claim by its ID.
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM claims WHERE id=?", (claim_id,))
    return cur.fetchone()

def list_claims(conn):
    """
    Retrieve all claims.
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM claims")
    return cur.fetchall()

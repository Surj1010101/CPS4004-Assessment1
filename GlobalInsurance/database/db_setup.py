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

def create_tables(conn):
    """Create tables for claims, policies, users, and an optional audit_logs table."""
    sql_create_claims_table = """
    CREATE TABLE IF NOT EXISTS claims (
        id INTEGER PRIMARY KEY,
        claim_number TEXT NOT NULL,
        date_of_claim TEXT,
        type_of_claim TEXT,
        description_of_accident TEXT,
        date_of_incident TEXT,
        location TEXT,
        incident_report TEXT,
        claim_amount REAL,
        approved_amount REAL,
        payment_details TEXT,
        claim_status TEXT,       -- e.g. "Pending", "Approved", "Rejected"
        resolution_notes TEXT,
        settlement_date TEXT
    );
    """

    sql_create_policies_table = """
    CREATE TABLE IF NOT EXISTS policies (
        id INTEGER PRIMARY KEY,
        policy_number TEXT NOT NULL,
        coverage_details TEXT,
        policy_limits TEXT,
        premium_amount REAL,
        payment_schedule TEXT,
        outstanding_payments REAL,
        beneficiary_info TEXT,
        coverage_exclusions TEXT
    );
    """

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL       
    );
    """

    sql_create_audit_table = """
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        action TEXT,
        timestamp TEXT
    );
    """

    try:
        cur = conn.cursor()
        cur.execute(sql_create_claims_table)
        cur.execute(sql_create_policies_table)
        cur.execute(sql_create_users_table)
        cur.execute(sql_create_audit_table)
        conn.commit()
    except Error as e:
        print(e)

def main():
    database = "global_insurance.db"
    conn = create_connection(database)
    if conn:
        create_tables(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()

import sqlite3
from sqlite3 import Error

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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def close_connection(conn):
    """ close the database connection
    """
    if conn:
        conn.close()

def main():
    database = r"global_insurance.db"

    sql_create_claims_table = """ CREATE TABLE IF NOT EXISTS claims (
                                     id integer PRIMARY KEY,
                                     claim_number text NOT NULL,
                                     date_of_claim text,
                                     type_of_claim text,
                                     description_of_accident text,
                                     date_of_incident text,
                                     location text,
                                     incident_report text,
                                     claim_amount real,
                                     approved_amount real,
                                     payment_details text
                                 ); """

    sql_create_policies_table = """CREATE TABLE IF NOT EXISTS policies (
                                     id integer PRIMARY KEY,
                                     policy_number text NOT NULL,
                                     coverage_details text,
                                     policy_limits text
                                 );"""

    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                     id integer PRIMARY KEY,
                                     username text NOT NULL,
                                     password text NOT NULL,
                                     role text NOT NULL
                                 );"""

    # create a database connection
    conn = create_connection(database)


    if conn is not None:
        # created claims table
        create_table(conn, sql_create_claims_table)

        # creatd policies table
        create_table(conn, sql_create_policies_table)

        #usersS table
        create_table(conn, sql_create_users_table)


        close_connection(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
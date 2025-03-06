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

def add_claim(conn, claim):
    """
    Create a new claim
    :param conn:
    :param claim:
    :return:
    """
    sql = ''' INSERT INTO claims(claim_number, date_of_claim, type_of_claim, description_of_accident)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, claim)
    conn.commit()
    return cur.lastrowid

def update_claim(conn, claim):
    """
    Update an existing claim
    :param conn:
    :param claim:
    :return:
    """
    sql = ''' UPDATE claims
              SET claim_number = ?,
                  date_of_claim = ?,
                  type_of_claim = ?,
                  description_of_accident = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, claim)
    conn.commit()

def main():
    database = r"global_insurance.db"

    # create a database connection
    conn = create_connection(database)

    # add a new claim
    with conn:
        claim = ('12345', '2025-03-04', 'Accident', 'Car accident on highway')
        claim_id = add_claim(conn, claim)
        print(f"Claim added with id: {claim_id}")

        # update the claim
        updated_claim = ('12345', '2025-03-04', 'Accident', 'Updated description', claim_id)
        update_claim(conn, updated_claim)
        print(f"Claim updated with id: {claim_id}")

if __name__ == '__main__':
    main()
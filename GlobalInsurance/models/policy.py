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

def add_policy(conn, policy):
    """
    Create a new policy
    :param conn:
    :param policy:
    :return:
    """
    sql = ''' INSERT INTO policies(policy_number, coverage_details, policy_limits)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, policy)
    conn.commit()
    return cur.lastrowid

def update_policy(conn, policy):
    """
    Update an existing policy
    :param conn:
    :param policy:
    :return:
    """
    sql = ''' UPDATE policies
              SET policy_number = ?,
                  coverage_details = ?,
                  policy_limits = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, policy)
    conn.commit()

def main():
    database = r"global_insurance.db"


    conn = create_connection(database)


    with conn:
        policy = ('POL12345', 'Full Coverage', '100000')
        policy_id = add_policy(conn, policy)
        print(f"Policy added with id: {policy_id}")


        updated_policy = ('POL12345', 'Full Coverage', '150000', policy_id)
        update_policy(conn, updated_policy)
        print(f"Policy updated with id: {policy_id}")

if __name__ == '__main__':
    main()